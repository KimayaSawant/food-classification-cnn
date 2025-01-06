import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import CNNModel 
import functools
import operator
import sqlite3
#import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Indian Food Image Classification ")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('img1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#
lbl = tk.Label(root, text="Indian Food Image Classification", font=('times', 35,' bold '), height=1, width=32,bg="Black",fg="white")
lbl.place(x=300, y=10)


#frame_display = tk.LabelFrame(root, text=" --Original Image-- ", width=200, height=200, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display.grid(row=0, column=0, sticky='nw')
#frame_display.place(x=250, y=80)

#frame_display1 = tk.LabelFrame(root, text=" --Result-- ", width=550, height=200, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display1.grid(row=0, column=0, sticky='nw')
#frame_display1.place(x=690, y=80)

#frame_display2 = tk.LabelFrame(root, text=" --Food Name-- ", width=200, height=100, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display2.grid(row=0, column=0, sticky='nw')
#frame_display2.place(x=460, y=80)


#frame_display3 = tk.LabelFrame(root, text=" --Ingradient-- ", width=500, height=380, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display3.grid(row=0, column=0, sticky='nw')
#frame_display3.place(x=10, y=300)

#frame_display4 = tk.LabelFrame(root, text=" --Procedure-- ", width=730, height=380, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display4.grid(row=0, column=0, sticky='nw')
#frame_display4.place(x=520, y=300)

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=10, y=80)


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 



def convert_str_to_tuple(tup):
    s = functools.reduce(operator.add, (tup))
    return s

def train_model():
 
    update_label("Model Training Start...............")
    
    start = time.time()

    X= CNNModel.main()
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    print(msg)

#root1=tk.Tk();

def test_model_proc(fn):
    from keras.models import load_model
    #from keras.optimizers import Adam

#    global fn
    
    IMAGE_SIZE = 64
    LEARN_RATE = 1.0e-4
    CH=1
    print(fn)
    if fn!="":
        # Model Architecture and Compilation
       
        model = load_model('food_model.h5')
            
        # adam = Adam(lr=LEARN_RATE, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0)
        # model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
        
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
        
        img = img.astype('float32')
        img = img / 255.0
        print('img shape:',img)
        prediction = model.predict(img)
        print(np.argmax(prediction))
        food=np.argmax(prediction)
        print(food)
        
        
        
        if food == 0:
            Cd="carrot_cake"
    
        elif food == 1:
            Cd="Mussels"
        elif food == 2:
            Cd="lobster_bisque"
        elif food == 3:
            Cd=" chocolate_cake"
        elif food == 4:
            Cd="crab_cakes"
        elif food == 5:
            Cd="fried_rice"
        elif food == 6:
            Cd="Ice_creame"
        elif food == 7:
            Cd="Garlic_Bread"
        elif food == 8:
            Cd="Pizza"
        elif food == 9:
            Cd="Samosa"
        elif food == 10:
            Cd="Onion_Rings"
      
        my_conn = sqlite3.connect('receipe.db')
        r_set=my_conn.execute("select food_name from foodreceipe where foodid =" + str(food) +"")    
        i=0 # row value inside the loop 
        for student in r_set: 
            for j in range(len(student)):
                        e =tk.Entry(root, width=10, fg='blue') 
                        e.grid(row=i, column=j) 
                        e.insert(END, student[j])
            i=i+1
        print(type(student))
        str1 = convert_str_to_tuple(student)
        print(str1)
        fname_label = tk.Label(root, text="Food Name:"+str(str1), width=30, font=("bold", 20), bg='light coral', fg='black')
        fname_label.place(x=730, y=100)    
        #-------------------------------------------------------    
        my_conn = sqlite3.connect('receipe.db')
        r_set1=my_conn.execute("select Ingradient from foodreceipe where foodid =" + str(food) +"")    
        i=0 # row value inside the loop 
        for student1 in r_set1: 
            for j in range(len(student1)):
                        e =tk.Entry(root, width=10, fg='blue') 
                        e.grid(row=i, column=j) 
                        e.insert(END, student1[j])
            i=i+1
        print(type(student1))
        str2 = convert_str_to_tuple(student1)
        print(str2)
        ing_label = tk.Label(root, text="Ingredient:\n"+str(str2), width=80, font=("bold", 10), bg='SlateBlue1', fg='black')
        ing_label.place(x=700, y=150)  
        #-------------------------------------------------------------
        my_conn = sqlite3.connect('receipe.db')
        r_set2=my_conn.execute("select Procedure from foodreceipe where foodid =" + str(food) +"")    
        i=0 # row value inside the loop 
        for student2 in r_set2: 
            for j in range(len(student2)):
                        e =tk.Entry(root, width=10, fg='blue') 
                        e.grid(row=i, column=j) 
                        e.insert(END, student2[j])
            i=i+1
        print(type(student2))
        str3 = convert_str_to_tuple(student2)
        print(str3)
        pro_label = tk.Label(root, text="Procedure:\n"+str(str3), width=90, font=("bold", 10), bg='SlateBlue1', fg='black',anchor='w')
        pro_label.place(x=700, y=430) 
        
        r_set=my_conn.execute("select Calries from foodreceipe where foodid =" + str(food) +"")    
        i=0 
        #update_cal(r_set)
       # row value inside the loop 
        for student in r_set: 
            for j in range(len(student)):
                e =tk.Entry(root, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, student[j])
            i=i+1
        print(type(student))
        str1 = convert_str_to_tuple(student)
        print(str1)
        cal_label = tk.Label(root, text="Calaries:"+str(str1), width=10, font=("bold", 25), bg='orchid1', fg='black')
        cal_label.place(x=10, y=500)
        ##-----------------FAT-------------------------------
        r_set1=my_conn.execute("select Fat from foodreceipe where foodid =" + str(food) +"")    
        i=0 
        #update_cal(r_set)
       # row value inside the loop 
        for student1 in r_set1: 
            for j in range(len(student1)):
                e =tk.Entry(root, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, student1[j])
            i=i+1
        print(type(student1))
        str5 = convert_str_to_tuple(student1)
        print(str5)
        fat_label = tk.Label(root, text="Fat:"+str(str5), width=10, font=("bold", 25), bg='orchid1', fg='black')
        fat_label.place(x=280, y=500)
        ###--------------------Protin----------------------------
        r_set3=my_conn.execute("select Protin from foodreceipe where foodid =" + str(food) +"")    
        i=0 
        #update_cal(r_set)
       # row value inside the loop 
        for student3 in r_set3: 
            for j in range(len(student1)):
                e =tk.Entry(root, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, student3[j])
            i=i+1
        print(type(student3))
        str3 = convert_str_to_tuple(student3)
        print(str3)
        fat_label3 = tk.Label(root, text="Protin:"+str(str3), width=10, font=("bold", 25), bg='orchid1', fg='black')
        fat_label3.place(x=10, y=600)
        #-------------------Carb---------------------------------
        r_set4=my_conn.execute("select carbohydrate from foodreceipe where foodid =" + str(food) +"")    
        i=0 
        #update_cal(r_set)
       # row value inside the loop 
        for student4 in r_set4: 
            for j in range(len(student4)):
                e =tk.Entry(root, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, student4[j])
            i=i+1
        print(type(student4))
        str4 = convert_str_to_tuple(student4)
        print(str4)
        fat_label4 = tk.Label(root, text="Carbohydrate:"+str(str4), width=15, font=("bold", 25), bg='orchid1', fg='black')
        fat_label4.place(x=230, y=600)
        
        r_set5 = my_conn.execute("select Solution from foodreceipe where foodid =" + str(food) +"")    
        i=0 
        #update_cal(r_set)
       # row value inside the loop 
        for student4 in r_set5: 
            for j in range(len(student4)):
                e =tk.Entry(root, width=10, fg='blue') 
                e.grid(row=i, column=j) 
                e.insert(END, student4[j])
            i=i+1
        print(type(student4))
        str5 = convert_str_to_tuple(student4)
        print(str5)
        fat_label4 = tk.Label(root, text="Solution:"+str(str5), font=("bold", 15), width = 150,bg='black', fg='white')
        fat_label4.place(x=20, y=750)
        
        
       # pro_label.pack()
        A = Cd 
        
        return A


# def clear_img():
    
#     img11 = tk.Label(frame_display, background='lightblue4',width=160,height=120)
#     img11.place(x=0, y=0)

def update_label(str_T):
    result_label = tk.Label(root, text=str_T, width=30, font=("bold", 20),bg='SkyBlue1',fg='black' )
    result_label.place(x=10, y=350)

# def train_model():
    
#     update_label("Model Training Start...............")
    
#     start = time.time()

#     X=Model_frm.main()
    
#     end = time.time()
        
#     ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
#     msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

#     update_label(msg)

    
def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=test_model_proc(fn)
        #from subprocess import call
        #call(["python","result.py"])
        
        X1="Selected Image is {0}".format(X)
        
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ X1 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
    
def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='E:\inverse_cooking\test_set', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=200
    imgpath = fileName
    fn = fileName


#        img = Image.open(imgpath).convert("L")
    img = Image.open(imgpath)
    
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
#        img = img / 255.0
#        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)


    x1 = int(img.shape[0])
    y1 = int(img.shape[1])


#
#        gs = cv2.cvtColor(cv2.imread(imgpath, 1), cv2.COLOR_RGB2GRAY)
#
#        gs = cv2.resize(gs, (x1, y1))
#
#        retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    img = tk.Label(root, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=300, y=80)
#        out_label.config(text=imgpath)

def convert_grey():
    global fn    
    IMAGE_SIZE=200
    
    img = Image.open(fn)
    img = img.resize((IMAGE_SIZE,200))
    img = np.array(img)
    
    x1 = int(img.shape[0])
    y1 = int(img.shape[1])

    gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)

    gs = cv2.resize(gs, (x1, y1))

    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    print(threshold)

    im = Image.fromarray(gs)
    imgtk = ImageTk.PhotoImage(image=im)
    
    # img2 = tk.Label(frame_display, image=imgtk, height=x1-50, width=y1-50)
    # img2.image = imgtk
    # img2.place(x=280, y=0)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    # img3 = tk.Label(frame_display, image=imgtk, height=x1-50, width=y1-50)
    # img3.image = imgtk
    # img3.place(x=580, y=0)



#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(frame_alpr, text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
button1.place(x=10, y=20)

# button3 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=12, height=1, font=('times', 15, ' bold '),bg="white",fg="black")
# button3.place(x=10, y=160)
#
button4 = tk.Button(frame_alpr, text="CNN_Prediction", command=test_model,width=15, height=1,bg="white",fg="black", font=('times', 15, ' bold '))
button4.place(x=10, y=80)
#
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=450, y=20)


exit = tk.Button(frame_alpr, text="Exit", command=window, width=15, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=10, y=140)



root.mainloop()