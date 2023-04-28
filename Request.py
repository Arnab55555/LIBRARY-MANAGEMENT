from tkinter import * 
import sqlite3
from tkinter import messagebox
from unicodedata import bidirectional  


def requesting(): 

        title = en1.get()
        author = en3.get()

        database_connection = sqlite3.connect("LIBRARY.db")
        database_cursor = database_connection.cursor()

        searchBooks = "insert into "+bookTable+" values('"+title+"','"+author+"');"

        print(searchBooks)

        # labelFrame = Frame(base,bg='black')
        # labelFrame.place(relx=0.1,rely=0.3,relheight=0.5,relwidth=0.8)
        # y = 0.25

        # Label(labelFrame, text="-------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
        try:
                print("Hello")
                database_cursor.execute(searchBooks)
                # database_connection.commit()
                # for i in database_cursor:
                #         print(i)
                #         print("hello")
                #         Label(labelFrame, text="%-10s%-40s%-10s%-10s%-10s%-20s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.07,rely=y)
                #         y += 0.1
                database_connection.commit()
                database_connection.close()
                messagebox.showinfo('Success',"Request of the book had been added successfully")

        except:
                # label35=Label(base,text = "No such book are available")
                # label35.place(x=270, y=200)
                messagebox.showinfo("Sorry","Failed to make the request")

        print(title)
        print(bidirectional)

def Request():

        global en1,en3,bookTable,base

       

        base = Tk()  
        base.geometry('800x500+10+20')  
        base.title("Requesting Book")  
                
        Canvas1 = Canvas(base)
                
        Canvas1.config(bg="indigo")
        Canvas1.pack(expand=True,fill=BOTH)
        bookTable = "REQUESTED_BOOK" 


        lb1= Label(base, text="BOOK Name", width=20, font=("arial",12))  
        lb1.place(x=150, y=120)  
        en1= Entry(base)  
        en1.place(x=500, y=120)  
        
        lb3= Label(base, text="Enter BOOK-ID", width=20, font=("arial",12))  
        lb3.place(x=150, y=190)  
        en3= Entry(base)  
        en3.place(x=500, y=190)  
        
        
        
      
        Button(base, text="REQUEST BOOK",command = requesting,width=15).place(x=330,y=300)  

        base.mainloop()  