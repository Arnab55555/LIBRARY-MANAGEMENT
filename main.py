from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

def amain():

    # Add your own database name and password here to reflect in the code
    # mypass = "root"
    # mydatabase="db"

    database_connection = sqlite3.connect("LIBRARY.db")
    database_cursor = database_connection.cursor()

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x600")

    # Take n greater than 0.25 and less than 5
    # same=True
    # n=0.25

    # Adding a background image
    # background_image =Image.open("IMAGES\libr.jpg")
    # [imageSizeWidth, imageSizeHeight] = background_image.size

    # newImageSizeWidth = int(imageSizeWidth*n)
    # if same:
    #     newImageSizeHeight = int(imageSizeHeight*n) 
    # else:
    #     newImageSizeHeight = int(imageSizeHeight/n) 


    # img = ImageTk.PhotoImage(background_image)

    # Canvas1 = Canvas(root)
    # canvas=Canvas(root,width=400,height=400,bg='white')
    # img = PhotoImage(file="pict.jpg")
    # canvas.create_image(0,0,anchor=NW,image=img)
    # canvas.pack(pady=20)

    # # Canvas1.create_image(280,300,image = img)      
    # Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
    # Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="  Welcome to \n LIBRARY", bg='black', fg='white', font=('Calibri',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook, font=('Calisto MT',11))
    btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

    btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete, font=('Calisto MT',11))
    btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

    btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View, font=('Calisto MT',11))
    btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook, font=('Calisto MT',11))
    btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook, font=('Calisto MT',11))
    btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

    root.mainloop()
