from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

# Add your own database name and password here to reflect in the code
# mypass = "root"
# mydatabase="db"

database_connection=sqlite3.connect("LIBRARY.db")
database_cursor = database_connection.cursor()

# Enter Table Names here
issueTable = "ISSUED_BOOKS" #Issue Table
bookTable = "BOOKS" #Book Table


# allBid = [] #List To store all Book IDs

def returnn():
    
    global SubmitBtn,labelFrame,lb1,bookInfo1,inf2,quitBtn,root,Canvas1,status,bid,num,n
    
    bid = bookInfo1.get()
    issueto = inf2.get()

    extractBid = "select BOOK_COUNT from "+bookTable+" where BOOK_ID="+bid+";"

    print(extractBid)
    try:
        database_cursor.execute(extractBid)
        # con.commit()
        for i in database_cursor:
            global no
            no = i[0]
            print (no)


        
        if (no >= 0):
            # checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            # cur.execute(checkAvail)
            # con.commit()
            # for i in cur:
            #     check = i[0]

            no = no + 1
            print(no)
            num = str(no)
            print(num)

            srt = "update "+bookTable+" SET BOOK_COUNT ='" +num+"' WHERE BOOK_ID=='"+bid+"';"
            print(srt)
            print(no)
                
            if (no > -1):
                print("hello")
                database_cursor.execute(srt)
                n = "ok"
                print(n)
                messagebox.showinfo("Success","Book has been returned successfully")
            else:
                messagebox.showinfo("Error","Book is not available")

    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    
    issueSql = "delete from "+issueTable+" where BOOK_ID = '"+bid+"'and USER_ID = '"+issueto+"';"
  
    # print(bid in allBid)
    # print(status)
    # updateStatus = "update "+bookTable+" set status = 'avail' where bid = '"+bid+"'"
    try:
        print(issueSql)
        print(type(n))
        if n == "ok":
            database_cursor.execute(issueSql)
            database_connection.commit()
            # cur.execute(updateStatus)
            # con.commit()
            messagebox.showinfo('Success',"Book Returned Successfully")
            root.destroy()
        else:
            # allBid.clear()
            messagebox.showinfo('Message',"Please check the book ID")
            root.destroy()
            return
    except:
        messagebox.showinfo("Error","The book id or user id is wrong, Try again")
    
    
    # allBid.clear()
    print(bid)
    print(issueto)
    # root.destroy()
    
def returnBook(): 
    
    global bookInfo1,inf2,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62)

    lb2 = Label(labelFrame,text="User Id: ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="Return",bg='#d1ccc0', fg='black',command=returnn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()