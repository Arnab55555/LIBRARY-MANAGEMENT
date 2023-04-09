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
issueTable = "ISSUED_BOOKS" 
bookTable = "BOOKS"
    
#List To store all Book IDs
# allBid = [] 

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status,bid
    
    bid = inf1.get()
    issueto = inf2.get()

    # issueBtn.destroy()
    # labelFrame.destroy()
    # lb1.destroy()
    # inf1.destroy()
    # inf2.destroy()
    
    
    extractBid = "select BOOK_COUNT from "+bookTable+" where BOOK_ID="+bid+";"
    updatet = "update BOOK SET BOOK_COUNT = 0 WHERE BOOK_ID="+bid+";"

    # global no
    # nu = no.get()

    # updatet = "update BOOKS set BOOK_COUNT = "+no+" where BOOK_ID= "+bid+";"

    print(extractBid)

    try:
        database_cursor.execute(extractBid)
        # database_connection.commit()
        for i in database_cursor:
            global no
            no = i[0]
            print (no)
        
        if (no > 0):
            # checkAvail = "select BOOK_COUNT from "+bookTable+" where bid = '"+bid+"'"
            # database_cursor.execute(extractBid)
            # database_connection.commit()
            # for i in database_cursor:
            #     check = i[0]
            no = no - 1
            print(no)
            # database_connection=sqlite3.connect("LIBRARY.db")
            # database_cursor = database_connection.cursor()
            # updt(no)
            if (no == 9):
                updatet = "update "+bookTable+" SET BOOK_COUNT = 9 WHERE BOOK_ID=='"+bid+"';"
                print(updatet)
                database_cursor.execute(updatet)
                database_connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully")
            elif (no == 8):
                updatet = "update "+bookTable+" SET BOOK_COUNT = 8 WHERE BOOK_ID=='"+bid+"';"
                print(updatet)
                database_cursor.execute(updatet)
                database_connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully")
            elif (no == 7):
                updatet = "update "+bookTable+" SET BOOK_COUNT = 7 WHERE BOOK_ID=='"+bid+"';"
                print(updatet)
                database_cursor.execute(updatet)
                database_connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully")
            elif (no == 6):
                updatet = "update "+bookTable+" SET BOOK_COUNT = 6 WHERE BOOK_ID=='"+bid+"';"
                print(updatet)
                database_cursor.execute(updatet)
                database_connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully")
            elif (no == 5):
                updatet = "update "+bookTable+" SET BOOK_COUNT = 5 WHERE BOOK_ID=='"+bid+"';"
                print(updatet)
                database_cursor.execute(updatet)
                database_connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully")
            elif (no == 4):
                updatet = "update "+bookTable+" SET BOOK_COUNT = 4 WHERE BOOK_ID=='"+bid+"';"
                print(updatet)
                database_cursor.execute(updatet)
                database_connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully")
            elif (no == 3):
                updatet = "update "+bookTable+" SET BOOK_COUNT = 3 WHERE BOOK_ID=='"+bid+"';"
                print(updatet)
                database_cursor.execute(updatet)
                database_connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully")
            elif (no == 2):
                updatet = "update "+bookTable+" SET BOOK_COUNT = 2 WHERE BOOK_ID=='"+bid+"';"
                print(updatet)
                database_cursor.execute(updatet)
                database_connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully")
            elif (no == 1):
                updatet = "update "+bookTable+" SET BOOK_COUNT = 1 WHERE BOOK_ID=='"+bid+"';"
                print(updatet)
                database_cursor.execute(updatet)
                database_connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully")
            elif (no == 0):
                updatet = "update "+bookTable+" SET BOOK_COUNT = 0 WHERE BOOK_ID=='"+bid+"';"
                print(updatet)
                database_cursor.execute(updatet)
                database_connection.commit()
                messagebox.showinfo("Success","Book has been issued successfully")
            # if (check > 0) :
            #     status = True
            # else:
            #     status = False
            else:
                messagebox.showinfo("Error","Book is not available")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"')"
    # show = "select * from "+issueTable
    
    # updateStatus = "update "+bookTable+" set BOOK_COUNT = 'issued' where bid = '"+bid+"'"
    try:
        if status == True:
            database_cursor.execute(issueSql)
            database_connection.commit()
            # cur.execute(updateStatus)
            # con.commit()
            messagebox.showinfo('Success',"Table has been updated Successfully")
            root.destroy()
        else:
            messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(issueto)
    
    # allBid.clear()


# def updt():
#     print("hello")
#     numb = no.get()
#     updatet = "update BOOKS set BOOK_COUNT = "+numb+" where BOOK_ID= "+bid+";"
#     print(updatet)
#     database_cursor.execute(updatet)


    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()