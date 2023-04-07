import tkinter
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Add your own database name and password here to reflect in the code
# mypass = "root"
# mydatabase="db"

database_connection = sqlite3.connect("LIBRARY.db")
database_cursor = database_connection.cursor()

# Enter Table Names here
bookTable = "BOOKS" 
    
def View(): 
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    #tree defining
    tree = ttk.Treeview(root)
    tree['show']="headings"


    tree['columns']=("BOOK_ID","BOOK_NAME","BOOK_TYPE","BOOK_PRICE","BOOK_COUNT","BOOK_AUTHOR")
    tree.column("BOOK_ID",width=50,minwidth=50,anchor=tkinter.CENTER)
    tree.column("BOOK_NAME",width=100,minwidth=100,anchor=tkinter.CENTER)
    tree.column("BOOK_TYPE",width=50,minwidth=50,anchor=tkinter.CENTER)
    tree.column("BOOK_PRICE",width=150,minwidth=150,anchor=tkinter.CENTER)
    tree.column("BOOK_COUNT",width=150,minwidth=150,anchor=tkinter.CENTER)
    tree.column("BOOK_AUTHOR",width=150,minwidth=150,anchor=tkinter.CENTER)

    tree.heading("BOOK_ID",    text="BOOK_ID",anchor=tkinter.CENTER)
    tree.heading("BOOK_NAME",  text="BOOK_NAME",anchor=tkinter.CENTER)
    tree.heading("BOOK_TYPE",  text="BOOK_TYPE",anchor=tkinter.CENTER)
    tree.heading("BOOK_PRICE", text="BOOK_PRICE",anchor=tkinter.CENTER)
    tree.heading("BOOK_COUNT", text="BOOK_COUNT",anchor=tkinter.CENTER)
    tree.heading("BOOK_AUTHOR",text="BOOK_AUTHOR",anchor=tkinter.CENTER)



    # labelFrame = Frame(root,bg='black')
    # labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    # y = 0.25
    
    # Label(labelFrame, text="%-10s%-70s%-10s%-10s%-10s%-20s"%('BID','Title','Type','Price','Count','Author'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    # Label(labelFrame, text="-------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getBooks = "select * from "+bookTable
    try:
        database_cursor.execute(getBooks)
        database_connection.commit()
        i = 0
        for ro in database_cursor:
            # Label(labelFrame, text="%-10s%-40s%-10s%-10s%-10s%-20s"%(i[0],i[1],i[2],i[3],i[4],i[5]),bg='black',fg='white').place(relx=0.07,rely=y)
            # y += 0.1
            tree.insert('',i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]))
            i = i+1
        tree.pack()
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()