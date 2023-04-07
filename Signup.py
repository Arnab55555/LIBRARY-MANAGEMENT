from tkinter import * 
import PIL
from PIL import ImageTk, Image
import ast
import sqlite3
# from APP import * 


def signUp():

    # App.root.destroy()

    base = Tk()  

    # Open window having dimension 100x100
    base.geometry('800x500+10+20')
    base.title("SIGNUP form")  

    labl_0 = Label(base, text="SIGN UP",width=20,font=("bold", 20))  
    labl_0.place(x=200,y=53)  
    
    lb1= Label(base, text="Enter Name", width=10, font=("arial",12))  
    lb1.place(x=200, y=120)  
    en1= Entry(base)  
    en1.place(x=380, y=120)  
    
    lb3= Label(base, text="Enter Email", width=10, font=("arial",12))  
    lb3.place(x=200, y=160)  
    en3= Entry(base)  
    en3.place(x=380, y=160)  
    
    
    lb5= Label(base, text="Select Gender", width=15, font=("arial",12))  
    lb5.place(x=180, y=240)  
    vars = IntVar()  
    Radiobutton(base, text="Male", padx=5,variable=vars, value=1).place(x=380, y=240)  
    Radiobutton(base, text="Female", padx =10,variable=vars, value=2).place(x=440,y=240)  
    Radiobutton(base, text="others", padx=15, variable=vars, value=3).place(x=510,y=240)  
    
    SELECT = ("ADMIN", "USER")  
    cv = StringVar()  
    drplist= OptionMenu(base, cv, *SELECT)  
    drplist.config(width=15)  
    cv.set("SELECT")  
    lb2= Label(base, text="SELECT", width=13,font=("arial",12))  
    lb2.place(x=170,y=280)  
    drplist.place(x=380, y=275)  
    
    lb6= Label(base, text="Enter Password", width=13,font=("arial",12))  
    lb6.place(x=200, y=320)  
    en6= Entry(base, show='*')  
    en6.place(x=380, y=320)  
    
    lb7= Label(base, text="Re-Enter Password", width=15,font=("arial",12))  
    lb7.place(x=200, y=360)  
    en7 =Entry(base, show='*')  
    en7.place(x=380, y=360)  
    
    Button(base, text="Register", width=10).place(x=300,y=400)  
    base.mainloop()  