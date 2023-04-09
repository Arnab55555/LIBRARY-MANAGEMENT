import tkinter
from tkinter import * 
import PIL
from PIL import ImageTk, Image
import ast
from tkinter import messagebox 
import sqlite3

# from APP import * 

database_connection = sqlite3.connect("LIBRARY.db")
database_cursor = database_connection.cursor()

def signuping():
    name = en1.get()
    mailing = en3.get()
    pas = en6.get()
    repas = en7.get()
    mobile=en8.get()
    # adm = vars.get()


    insertAdmin = "insert into ADMIN(ADMIN_NAME,PASSWORD,EMAIL,MOBILE_NO) values('"+name+"','"+pas+"','"+mailing+"','"+mobile+"');"
    insertUser = "insert into USER(USER_NAME,PASSWORD,EMAIL,MOBILE_NO) values('"+name+"','"+pas+"','"+mailing+"','"+mobile+"');"

    if (vars == 2):
        if (repas == pas):
            print(insertAdmin)
            print(vars)
            try:
                database_cursor.execute(insertAdmin)
                messagebox.showinfo("Success","You have registered successfully")
            except:
                messagebox.showinfo("Error","Sorry you are not able to register")
        else:
            messagebox.showinfo("Error","Enter your both password correctly")
    else:
        if (repas == pas):
            print(insertUser)
            try:
                database_cursor.execute(insertUser)
                messagebox.showinfo("Success","You have registered successfully")
            except:
                messagebox.showinfo("Error","Sorry you are not able to register")
        else:
            messagebox.showinfo("Error","Enter your both password correctly")







def signUp():

    global en7,en1,en3,en6,en8


    # App.root.destroy()

    base = Tk()  


    # Open window having dimension 100x100
    base.geometry('800x500+10+20')
    base.title("SIGNUP form")

    # canvas = Canvas(base,width=400,heigh=400,bg="black")
    # img = PhotoImage(file="pict.jpg")
    # canvas.create_image(0,0,anchor=NW,image=img)
    # canvas.pack(pady=20)  

    labl_0 = Label(base, text="SIGN UP",width=20,font=("bold", 20))  
    labl_0.place(x=230,y=60)  
    
    lb1= Label(base, text="Enter Name", width=10, font=("arial",12))  
    lb1.place(x=200, y=120)  
    en1= Entry(base)  
    en1.place(x=380, y=120)  
    
    lb3= Label(base, text="Enter Email", width=10, font=("arial",12))  
    lb3.place(x=200, y=160)  
    en3= Entry(base)  
    en3.place(x=380, y=160)  
    
    
    
    lb5= Label(base, text="REGISTER AS ", width=15, font=("arial",12))  
    lb5.place(x=180, y=240)  
    vars = tkinter.IntVar()  
    r1=Radiobutton(base, text="USER", padx=5,variable=vars, value=1).place(x=380, y=240)
    r2=Radiobutton(base, text="ADMIN", padx =10,variable=vars, value=2).place(x=440,y=240)  
    

    
    
    lb6= Label(base, text="Enter Password", width=13,font=("arial",12))  
    lb6.place(x=200, y=280)  
    en6= Entry(base, show='*')  
    en6.place(x=380, y=280)  
    
    lb7= Label(base, text="Re-Enter Password", width=15,font=("arial",12))  
    lb7.place(x=200, y=320)  
    en7 =Entry(base, show='*')  
    en7.place(x=380, y=320)  
    
    lb8= Label(base, text="MOBILE NUMBER", width=15,font=("arial",12))  
    lb8.place(x=200, y=360)  
    en8 =Entry(base, show='*')  
    en8.place(x=380, y=360)  

    Button(base, text="Register",command=signuping, width=20).place(x=300,y=400)  
    base.mainloop()  