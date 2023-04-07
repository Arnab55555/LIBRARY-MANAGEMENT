from tkinter import * 
import sqlite3 
base = Tk()  
base.geometry("500x500")  
base.title("registration form")  
  

database_connection = sqlite3.connect("LIBRARY.db")
database_cursor = database_connection.cursor()

bookTable = "BOOKS" 
bid = bookInfo1.get()
title = bookInfo2.get()

global bookInfo1,bookInfo2,Canvas1,con,cur,bookTable,root


try:
        database_cursor.execute(getBooks)
        database_connection.commit()
        for i in database_cursor:
            Label(labelFrame, text="%-10s%-40s%-10s%-10s%-10s%-20s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
except:
        messagebox.showinfo("Failed to fetch files from database")

lb1= Label(base, text="BOOK Name", width=20, font=("arial",12))  
lb1.place(x=50, y=120)  
en1= Entry(base)  
en1.place(x=270, y=120)  
  
lb3= Label(base, text="Enter BOOK-ID", width=20, font=("arial",12))  
lb3.place(x=50, y=160)  
en3= Entry(base)  
en3.place(x=270, y=160)  
  
 
  
Button(base, text="SEARCH", width=10).place(x=100,y=400)  
Button(base, text="REQUEST", width=10).place(x=270,y=400)  
base.mainloop()  