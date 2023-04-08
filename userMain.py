import tkinter
from tkinter import *
from requestsear import *
from Request import *

def u_main():
    
    root = Tk()
    root.title("test")
    root.minsize(width=400,height=400)
    root.geometry("600x600")

    btn2 = Button(root,text="SEARCH BOOK",bg='black', fg='white', command=requestEar, font=('Calisto MT',11))
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)


    btn3 = Button(root,text="REQUEST BOOK",bg='black', fg='white', command=Request, font=('Calisto MT',11))
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)


    root.mainloop()
