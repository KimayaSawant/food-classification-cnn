import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
from tkinter import messagebox as ms

global fn

fn=""


##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title(" GUI_Master")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('slide2.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

#
label_l2 = tk.Label(root, text="Indian Food Image Classification with Transfer Learning",font=("times", 30, 'bold'),
                    background="Green", fg="white", width=70, height=2)
label_l2.place(x=0, y=0)








frame_alpr = tk.LabelFrame(root, text=" Image Processing ", width=1000, height=450, bd=5, font=('times', 14, ' bold '),bg="grey",fg="black")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=400, y=200)




def openimage():
   
    global fn
    fileName = askopenfilename(initialdir='E://30%-food-classification//dataset', title='Select image for Aanalysis ',
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



    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(im)
    img = tk.Label(frame_alpr, image=imgtk, height=250, width=250)
    img.image = imgtk
    img.place(x=30, y=80)
  
#############################################################################    

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
    
    #result_label1 = tk.Label(root, image=imgtk, width=250, font=("bold", 25), bg='bisque2', fg='black',height=250)
    #result_label1.place(x=300, y=400)
    img2 = tk.Label(frame_alpr, image=imgtk, height=250, width=250,bg='white')
    img2.image = imgtk
    img2.place(x=360, y=80)

    im = Image.fromarray(threshold)
    imgtk = ImageTk.PhotoImage(image=im)

    img3 = tk.Label(frame_alpr, image=imgtk, height=250, width=250)
    img3.image = imgtk
    img3.place(x=700, y=80)
    #result_label1 = tk.Label(root, image=imgtk, width=250,height=250, font=("bold", 25), bg='bisque2', fg='black')
    #result_label1.place(x=300, y=400)





def window():
  root.destroy()
  
  


button4 = tk.Button(root, text="Exit", command=window, width=12, height=1,font=('times 15 bold'),bd=0,bg="red", fg="white")
button4.place(x=50, y=550)

#####################################################################################################################


button1 = tk.Button(root, text=" Select_Image ", command=openimage,width=15, height=1, font=('times', 15, ' bold '),bg="black",fg="white")
button1.place(x=50, y=350)

button2 = tk.Button(root, text="Image_preprocess", command=convert_grey, width=15, height=1, font=('times', 15, ' bold '),bg="black",fg="white")
button2.place(x=50, y=450)

#####################################################################################################################





root.mainloop()