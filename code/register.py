# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:57:26 2021

@author: HP
"""
from PIL import Image, ImageTk
from tkinter import *
import tkinter.messagebox as tmsg
import mysql.connector
from datetime import date
import os
import dataset_capture as dc
#import login as lg
global f1
global name,password
def register():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    mycursor = mydb.cursor()
    def update():  
        name=name_var.get()
        password=password_var.get()
        sql="INSERT INTO login(username,password) VALUES(%s,%s)"
        value=(name,password)
        mycursor.execute(sql,value)
        mydb.commit()
        root.destroy()
        os.system("python face_training.py")
        

    global root
    root=Tk()
    root.geometry("150x200")
    root.maxsize(580,550)
    root.minsize(580,550)
    root.title("REGISTERATION FORM")
    photo = ImageTk.PhotoImage(file=r"images\\login.png")

    l_login=Label(image=photo)
    f1=Frame(l_login,pady="20",padx="20")
    l0=Label(f1,text="Registration Form",bg="orange",fg="blue",font="lucida 10 bold",width="35",pady="4").grid(columnspan=3,row=0,pady="15")
    name_var=StringVar()
    lb1 =Label(f1,text="Enter ID: ",font="lucida 10 bold").grid(column=0,row=1,pady="4")
    #mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    #mycursor = mydb.cursor()
    
        
    e1 =Entry(f1,textvariable=name_var,width="28").grid(column=1,row=1)
    password_var=StringVar()
    l2=Label(f1,text="Password : ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
    e2=Entry(f1,textvariable=password_var,show="*",width="28")
    e2.grid(column=1,row=2)
    
    
    
# inte = IntVar()
    #textvariable=inte
    

    btn=Button(f1,text="Submit",bg="green",fg="white",width="10",font="lucida 10 bold",command=update )
    btn.grid(columnspan=3,row=8,pady="10")
    l_login.pack(ipadx="100",fill=BOTH)
    f1.pack(pady="165")
    #update(name,password)
    #mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    #mycursor = mydb.cursor()
   
    root.mainloop()

    