# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 20:25:59 2021

@author: HP
"""
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.messagebox as tmsg
import os
import mysql.connector
import Repage as fp

def deleting():
    
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    mycursor = mydb.cursor()
    def pinga():
       roll_no=venroll.get()    
       if(roll_no==""):
            tmsg.showinfo("Empty","Fill the field!!!")
            
       else:
                    sql="Delete from Attend where roll_no=%s"
                    value=roll_no
                    mycursor.execute(sql,(value,))
                    mydb.commit()
                    tmsg.showinfo("Done","Deleted done!!!")
    def back():
        root.destroy()
        fp.firstpage()
    root=Tk()
    root.title("DELETING MEMEBER")
    root.geometry("150x200")
    root.maxsize(580,550)
    root.minsize(580,550)
    photo = ImageTk.PhotoImage(file=r"images\\register.png")

    ld=Label(image=photo)
    f2=Frame(ld,padx="20",pady="20")
    l0=Label(f2,text="Student details",bg="orange",fg="blue",font="lucida 15 bold",width="35",pady="4")
    l0.grid(columnspan=3,row=0,pady="15")
    l1=Label(f2,text="Roll_no: ",font="lucida 10 bold").grid(column=0,row=1,pady="4")
    venroll = StringVar()
    e1=Entry(f2,textvariable=venroll,width="32")
    e1.grid(column=1,row=1)
    btn2=Button(f2,text="Delete",bg="blue",fg="white",width="10",font="lucida 10 bold",command=pinga)
    
    btn2.grid(columnspan=1,row=6,pady="20")
    btn3=Button(f2,text="Back",bg="green",fg="white",width="10",font="lucida 10 bold",command=back)
    
    btn3.grid(column=2,row=6,pady="20")
    ld.pack(ipadx="100",fill=BOTH)
    f2.pack(pady="165")
    root.mainloop()
