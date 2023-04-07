from tkinter import *  
base = Tk()  
base.geometry("500x500")  
base.title("registration form")  
  
lb1= Label(base, text="BOOK Name", width=20, font=("arial",12))  
lb1.place(x=50, y=120)  
en1= Entry(base)  
en1.place(x=270, y=120)  
  
lb3= Label(base, text="Enter BOOK-ID", width=20, font=("arial",12))  
lb3.place(x=50, y=160)  
en3= Entry(base)  
en3.place(x=270, y=160)  
  
 
  
Button(base, text="SEARCH", width=10).place(x=100,y=250)  
Button(base, text="REQUEST", width=10).place(x=270,y=250)  
base.mainloop()  