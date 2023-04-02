import os
import email
from email.message import EmailMessage
import ssl
import smtplib


from tkinter import messagebox
import sqlite3






# email_sender = 'autolibpy@gmail.com'
# email_password = 'epemdruoebcgmtta'
# email_reciever = 'deadsoul079@gmail.com'

# subject = 'test mail'
# body = """
# I am trying email automation using python.
# hi amit!!!!
# """


# em = EmailMessage()
# em['From'] = email_sender
# em['To']  = email_reciever
# em['subject'] = subject
# em.set_content(body)

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_reciever, em.as_string())


database_connection = sqlite3.connect("LIBRARY.db")
database_cursor = database_connection.cursor()

test = 'the merchant of veniece'

try:
    database_cursor.execute('''SELECT EMAIL FROM USER;''')
    for i in database_cursor:
        print(i[0])
       

        email_sender = 'autolibpy@gmail.com'
        email_password = 'epemdruoebcgmtta'
        email_reciever = i[0]

        print(email_reciever)

        subject = 'test mail'
        body = """
        I am trying email """ +test+ """automation using python.
        hi amit!!!!
        """


        em = EmailMessage()
        em['From'] = email_sender
        em['To']  = email_reciever
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_reciever, em.as_string())

        

except:
    print("incorrect automation")
    