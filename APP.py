from tkinter import *
from tkinter import messagebox 
import PIL
from PIL import ImageTk, Image
import ast
import sqlite3
from main import *

# img = ImageTk.PhotoImage(Image.open("IMAGES/signup.jpg"))
# Label(root,image=img,border=0,bg='white').place(x=-90,y=-80)

def app():
    root=Tk()
    root.title("signup")
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')
    root.resizable(False,False)

    user=StringVar()
    code=StringVar()



    def signin():
        Username = user.get()
        print(Username)
        Password = code.get()
        print(Password)
        database_connection=sqlite3.connect("LIBRARY.db")
        database_cursor = database_connection.cursor()
        database_cursor.execute("select * from USER where USER_NAME=? and PASSWORD=? ",(Username,Password))
        result=database_cursor.fetchone()



        if result:
            root.destroy()
            return amain()
            
        #    screen=Toplevel(root)
        #    screen.title("App")
        #    screen.geometry('925x500+300+200')
        #    screen.config(bg="white")
        #    print("You have successfully logged in")
        #    Label(screen,text='Hello Everyone!',bg='#fff',font=('calibri(Body)',50,'bold')).pack(expand=True)
        #    screen.mainloop()

        #elif Username!='admin' and password!='1234':
           # messagebox.showerror("Invalid","Invalid username and password")

        #elif  password!='1234':
            #messagebox.showerror("Invalid","Invalid password") 

        else:
            messagebox.showerror("Invalid","Please input correct username or password...!")
            database_connection.commit()
            database_connection.close()
        
        

    #  img = ImageTk.PhotoImage(Image.open("IMAGES/signup.jpg"))
    #  Label(root,image=img,border=0,bg='white').place(x=-90,y=-80)

    frame=Frame(root,width=350,height=350,bg="white")
    frame.place(x=520,y=70)

    heading=Label(frame,text='sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=5)

    ######################-----------------------------------------------------------------

    def on_enter(e):
        user.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user= Entry(frame,width=35,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11,))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    ######################---------------------------------------------------------------------

    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
        name=user.get()
        if name=='':
            code.insert(0,'password')
    code= Entry(frame,width=35,fg='black',border=2,bg="white",font=('Microsoft YaHei UI Light',11,),show='*')
    code.place(x=30,y=150)
    code.insert(0,'password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
    #####################------------------------------------------------------------------------

    Button(frame,width=39,pady=7,text='sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)

    root.mainloop()

