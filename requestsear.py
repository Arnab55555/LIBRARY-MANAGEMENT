import tkinter
from tkinter import ttk
from tkinter import * 
import sqlite3
from tkinter import messagebox  
from Request import *



def searh(): 

        title = en1.get()
        bid = en3.get()

        database_connection = sqlite3.connect("LIBRARY.db")
        database_cursor = database_connection.cursor()

        searchBooks = "SELECT * from '"+bookTable+"' where BOOK_NAME == '"+title+"' or BOOK_ID = '"+bid+"';"

        print(searchBooks)


        try:
              
                database_cursor.execute(searchBooks)
                database_connection.commit()
                i = 0
                for ro in database_cursor:
                        tree.insert('',i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
                        i = i+1
                # database_connection.close()
                messagebox.showinfo('Success',"Book found successfully")

        except:
                # label35=Label(base,text = "No such book are available")
                # label35.place(x=270, y=200)
                messagebox.showinfo("Sorry","Sorry no such books available in the library")

        print(title)
        print(bid)

def requestEar():

        global en1,en3,bookTable,base,tree

       

        base = Tk()  
        base.geometry("600x500")  
        base.title("searching book")  

        bookTable = "BOOKS" 


        lb1= Label(base, text="BOOK Name", width=20, font=("arial",12))  
        lb1.place(x=50, y=120)  
        en1= Entry(base)  
        en1.place(x=270, y=120)  
        
        lb3= Label(base, text="Enter BOOK-ID", width=20, font=("arial",12))  
        lb3.place(x=50, y=160)  
        en3= Entry(base)  
        en3.place(x=270, y=160)  
        
        tree = ttk.Treeview(base)
        tree['show']="headings"

        s = ttk.Style(base)
        s.theme_use("clam")


        tree['columns']=("BOOK_ID","BOOK_NAME","BOOK_TYPE","BOOK_PRICE","BOOK_COUNT","BOOK_AUTHOR")
        tree.column("BOOK_ID",width=50,minwidth=50,anchor=tkinter.CENTER)
        tree.column("BOOK_NAME",width=100,minwidth=100,anchor=tkinter.CENTER)
        tree.column("BOOK_TYPE",width=50,minwidth=50,anchor=tkinter.CENTER)
        tree.column("BOOK_PRICE",width=50,minwidth=50,anchor=tkinter.CENTER)
        tree.column("BOOK_COUNT",width=50,minwidth=50,anchor=tkinter.CENTER)
        tree.column("BOOK_AUTHOR",width=100,minwidth=100,anchor=tkinter.CENTER)

        tree.heading("BOOK_ID",    text="ID",anchor=tkinter.CENTER)
        tree.heading("BOOK_NAME",  text="NAME",anchor=tkinter.CENTER)
        tree.heading("BOOK_TYPE",  text="TYPE",anchor=tkinter.CENTER)
        tree.heading("BOOK_PRICE", text="PRICE",anchor=tkinter.CENTER)
        tree.heading("BOOK_COUNT", text="COUNT",anchor=tkinter.CENTER)
        tree.heading("BOOK_AUTHOR",text="AUTHOR",anchor=tkinter.CENTER)

        tree.place(relx=0.1,rely=0.4, relwidth=0.8, relheight=0.3)

        
        
        Button(base, text="SEARCH",command = searh, width=10).place(x=100,y=400)  
        Button(base, text="MAKE REQUEST",command=requesting, width=10).place(x=270,y=400)  
        base.mainloop() 