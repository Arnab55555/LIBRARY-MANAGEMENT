# import everything from tkinter module
from tkinter import *
from PIL import ImageTk, Image

# create a tkinter window
root = Tk()			

# Open window having dimension 100x100
root.geometry('800x500+10+20')



img = ImageTk.PhotoImage(Image.open("pl.jpg"))
Label(root,image=img,border=0,bg='white').place(x=0,y=0)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

sign_up= Button(width=20,text='USER',border=0,bg='light grey',cursor='hand2',fg='#57a1f8',bd = '20')
sign_up.place(x=495,y=180)

sign_up= Button(width=20,text='ADMIN',border=0,bg='light grey',cursor='hand2',fg='#57a1f8',bd = '20')
sign_up.place(x=495,y=270)


label=Label(frame,text="Don,t have an accout?",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=10,y=270)

sign_up= Button(frame,width=6,text='sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=140,y=270)

root.mainloop()
