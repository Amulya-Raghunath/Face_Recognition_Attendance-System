# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 08:09:45 2021

@author: HP
"""

from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import os
import mysql.connector
import Repage as fp
#global venroll

def view():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    mycursor = mydb.cursor()
    root=Tk()
    root.title("VIEW DETAILS")
    root.geometry("150x200")
    root.maxsize(580,550)
    root.minsize(580,550)
    photo = ImageTk.PhotoImage(file=r"images\\register.png")

    ld=Label(image=photo)
    f2=Frame(ld,pady="25",padx="25")   
    def search():
        roll_no=venroll.get()    
        if(roll_no==""):
            tmsg.showinfo("Empty","Fill the field!!!")
            
        else:
            mycursor.execute("Select * from Attend")
            myresult = mycursor.fetchall()
            mydb.commit()
            for r in myresult:
                if(roll_no==r[1]):
                    l2=Label(f2,text="Name: ",font="lucida 10 bold").grid(column=0,row=6,pady="4")
                    a2=Label(f2,text=r[0],font="lucida 10 bold").grid(column=1,row=6,pady="4")
                    l3=Label(f2,text="Roll_no: ",font="lucida 10 bold").grid(column=0,row=7,pady="4")
                    a3=Label(f2,text=r[1],font="lucida 10 bold").grid(column=1,row=7,pady="4")
                    l4=Label(f2,text="Class: ",font="lucida 10 bold").grid(column=0,row=8,pady="4")
                    a4=Label(f2,text=r[2],font="lucida 10 bold").grid(column=1,row=8,pady="4")
                    l5=Label(f2,text="Status as of today: ",font="lucida 10 bold").grid(column=0,row=9,pady="4")
                    a5=Label(f2,text=r[3],font="lucida 10 bold").grid(column=1,row=9,pady="4")
                    
        #1root.destroy()           
        
        
        
                
    def back():
        root.destroy()
        fp.firstpage()
        
         
                
               
                
          
    
    #root.title("View window")
    
    l0=Label(f2,text="View Details",bg="orange",fg="blue",font="lucida 10 bold",width="35",pady="4").grid(columnspan=3,row=0,pady="15")
    l1=Label(f2,text="Roll_no: ",font="lucida 10 bold").grid(column=0,row=1,pady="4")
    venroll = StringVar()
    e1=Entry(f2,textvariable=venroll,width="28").grid(column=1,row=1)
    btn=Button(f2,text="Search",bg="green",fg="white",width="10",font="lucida 10 bold",command=search)
    btn.grid(columnspan=3,row=5,pady="20")
    btn2=Button(f2,text="Back",bg="blue",fg="white",width="10",font="lucida 10 bold",command=back)
    btn2.grid(columnspan=1,row=5,pady="20")
    ld.pack(ipadx="100",fill=BOTH)
    f2.pack(pady="115")
    root.mainloop()

