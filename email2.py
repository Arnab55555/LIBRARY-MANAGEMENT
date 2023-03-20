import os
import email
from email.message import EmailMessage
import ssl
import smtplib



email_sender = 'autolibpy@gmail.com'
email_password = 'epemdruoebcgmtta'
email_reciever = 'mumbaikarprerna@gmail.com'

subject = 'test mail'
body = """
I am trying email automation using python.
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
