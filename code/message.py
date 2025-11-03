# Python code to illustrate Sending mail from 
# your Gmail account 
from tkinter import *
import time
import datetime
import tkinter.messagebox as tmsg
import smtplib
import os
import mysql.connector
def message():
    def mail(name,receiv):
        EMAIL=os.environ.get('USER')
        PASSW=os.environ.get('PASSW')  
# creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
  
# start TLS for security
        s.starttls()
        s.ehlo()  
# Authentication
        s.login(EMAIL, PASSW)
        ts=time.time()

        st=datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
  
# message to be sent
        subject="Absent notification"
        body="Your ward "+name+" is absent today "+st
        message = f'Subject:{subject}\n\n{body}'
    #gro=['rrjamadagni@gmail.com','sudha1499@gmail.com','1jt17is004@jyothyit.ac.in']  
# sending the mail
        s.sendmail(EMAIL,receiv, message)
        
        s.quit()
    group=[]
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    mycursor = mydb.cursor()
    mycursor.execute("Select * from Attend")
    myresult = mycursor.fetchall()
    mydb.commit()
    for r in myresult:
        if(r[3]=="Absent"):
            mail(r[0],r[5])
    print("Successfully sent")
    tmsg.showinfo("Success","Mail sent successfully")

# terminating the session
  