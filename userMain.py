import tkinter
from tkinter import *
from requestsear import *


root = Tk()
root.title("test")
root.minsize(width=400,height=400)
root.geometry("600x600")

btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=requestEar, font=('Calisto MT',11))
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)


root.mainloop()