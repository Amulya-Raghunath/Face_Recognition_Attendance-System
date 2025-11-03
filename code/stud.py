# -*- coding: utf-8 -*-
"""
Created on Sat May  8 16:41:11 2021

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:50:51 2021

@author: HP
"""
from PIL import Image, ImageTk
from tkinter import *
import tkinter.messagebox as tmsg
import mysql.connector
#import Auth as au
import update1 as up
#import View as vi
import os


global root
def neti(roll_no):
    root=Tk()

    def logout():
        root.destroy()
        os.system("python Student.py")
    def modify1():
        root.destroy()
        up.modify()
    





    global lid,lpass
# creating fixed geometry of the 
# tkinter window with dimensions 150x200 
    root.geometry("150x200")
    root.maxsize(580,550)
    root.minsize(580,550)

#providing a title
    root.title("STUDENT PORTAL")
#pic = Image.open("images\\wallpaper.png")
#pic=pic.resize((768,512), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(file=r"images\\login.png")

    l_login=Label(image=photo)
    f_login=Frame(l_login,pady="25",padx="25") #cretaing a Frame which can expand according to the size of the window
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Attend")
    rows=mycursor.fetchall()
    for r in rows:
        if(roll_no==r[1]):
            l2=Label(f_login,text="Name: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
            a2=Label(f_login,text=r[0],font="lucida 10 bold").grid(column=1,row=2,pady="4")
            l3=Label(f_login,text="Roll_no: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
            a3=Label(f_login,text=r[1],font="lucida 10 bold").grid(column=1,row=3,pady="4")
            l4=Label(f_login,text="Class: ",font="lucida 10 bold").grid(column=0,row=4,pady="4")
            a4=Label(f_login,text=r[2],font="lucida 10 bold").grid(column=1,row=4,pady="4")
            l5=Label(f_login,text="Status as of today: ",font="lucida 10 bold").grid(column=0,row=5,pady="4")
            a5=Label(f_login,text=r[3],font="lucida 10 bold").grid(column=1,row=5,pady="4")

    #btn=Button(f_login,text="View Attendance",bg="green",fg="white",width="15",font="lucida 10 bold")#,command=Login)
    #btn.grid(columnspan=1,row=6,pady="10")
    btn=Button(f_login,text="Update",bg="blue",fg="white",width="10",font="lucida 10 bold",command=modify1)
    btn.grid(columnspan=1,row=6,pady="10")
    btn=Button(f_login,text="Logout",bg="red",fg="white",width="10",font="lucida 10 bold",command=logout)
    btn.grid(columnspan=1,row=7,pady="10")
    l_login.pack(ipadx="110",fill=BOTH)
    f_login.pack(pady="115")
    root.mainloop()
