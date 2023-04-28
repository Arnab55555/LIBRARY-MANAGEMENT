# import everything from tkinter module
from tkinter import *
from Signup import *
from tkinter import messagebox 
import PIL
from PIL import ImageTk, Image
import ast
import sqlite3
from userSignIn import *
from APP import *

# create a tkinter window
root = Tk()			

# Open window having dimension 100x100
root.geometry('800x500+10+20')

bg_image = Image.open("IMAGES/user.jpg")

# Calculate the new size of the image
new_size = (bg_image.size[0]//4, bg_image.size[1]//4)

# Resize the image using subsample
bg_image = bg_image.resize(new_size, Image.LANCZOS)

# Create a PhotoImage object from the resized image
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label with the background image
background_label = Label(root, image=bg_photo)
background_label.place(x=0, y=-30, relwidth=1.2, relheight=1.2)

frame=Frame(root,width=250,height=250,bg="white")
frame.place(x=30,y=120)

sign_up= Button(width=20,text='ADMIN',border=0,bg='navy blue',cursor='hand2',fg='white',bd = '25',command=app)
sign_up.place(x=50,y=160)

sign_up= Button(width=20,text='STUDENT',border=0,bg='navy blue',cursor='hand2',fg='white',bd = '25',command=Usersignin)
sign_up.place(x=50,y=250)


label=Label(frame,text="Don,t have an accout?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=20,y=220)

sign_up= Button(frame,width=6,text='sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8', command=signUp)
sign_up.place(x=150,y=220)

root.mainloop()
