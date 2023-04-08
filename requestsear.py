from tkinter import * 
import sqlite3
from tkinter import messagebox  



def searh(): 

        title = en1.get()
        bid = en3.get()

        database_connection = sqlite3.connect("LIBRARY.db")
        database_cursor = database_connection.cursor()

        searchBooks = "SELECT * from '"+bookTable+"' where BOOK_NAME == '"+title+"' or BOOK_ID = '"+bid+"';"

        print(searchBooks)

        labelFrame = Frame(base,bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relheight=0.5,relwidth=0.8)
        y = 0.25

        Label(labelFrame, text="-------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
        try:
              
                database_cursor.execute(searchBooks)
                # database_connection.commit()
                for i in database_cursor:
                        print(i)
                        
                        Label(labelFrame, text="%-10s%-40s%-10s%-10s%-10s%-20s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.07,rely=y)
                        y += 0.1
                database_connection.commit()
                database_connection.close()
                messagebox.showinfo('Success',"Book found successfully")

        except:
                # label35=Label(base,text = "No such book are available")
                # label35.place(x=270, y=200)
                messagebox.showinfo("Failed to fetch files from database")

        print(title)
        print(bid)

def requestEar():

        global en1,en3,bookTable,base

       

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
        
        
        
        Button(base, text="SEARCH",command = searh, width=10).place(x=100,y=400)  
        Button(base, text="REQUEST", width=10).place(x=270,y=400)  
        base.mainloop() 