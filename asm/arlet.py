from email.message import EmailMessage
from django.conf import  settings
import smtplib


def email_arlet(subject, body, to):
    msg= EmailMessage()
    msg.set_content(body)
    msg['subject']= subject
    msg['to']= to

    user = "dmutemachani@timb.co.zw"
    msg['from']= user
    password="Dannydee1"

    server=smtplib.SMTP("172.18.170.6")
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()

if __name__ == "__main__":
    email_arlet("hey","Hello world","danielmshaty@gmail.com")
   
    
