# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 13:24:50 2021

@author: HP
"""
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import os
import mysql.connector
import face_recognition as fr

import dataset_capture as dc
import firstpage as fp
global root
def add_new():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    mycursor = mydb.cursor()
    def change():
        name=name_var.get()
        roll_no=venroll.get()
        classi=vyear.get()
        status=vstate.get()
        datei=vdate.get()
        emailid=vemail.get()
        if(name=="" or roll_no==" "or classi==" " or status==" " or datei==" " or emailid==""):
            tmsg.showwarning("Missing","Fill all the fields!!")
        else:
            sql="Insert into Attend(name,roll_no,class,status,date,p_email) values(%s,%s,%s,%s,%s,%s)"
            values=(name,roll_no,classi,status,datei)
            mycursor.execute(sql,values)
            mydb.commit()
            tmsg.showinfo("Successful","Insertion done!!!")
            
            tmsg.showinfo("Photo","Please take the photos!!")
            dc.dataset_capture()
            
    def back():
        root.destroy()
        fp.firstpage()
            
        
    root=Tk()
    root.title("ADD STUDENT")
    #pic = Image.open("images\\wallpaper.png")
    #pic=pic.resize((768,512), Image.ANTIALIAS)
    c=Canvas(root,bg="blue",height=481,width=768)
    fn=PhotoImage(file="images\\register.png")
    c.create_image(0,0,image=fn,anchor="nw")
    l0=Label(root,text="Student details",bg="orange",fg="blue",font="lucida 15 bold",width="35",pady="4")
    l0_can=c.create_window(200,10,anchor="nw",window=l0)
    l1=Label(root,text="Name: ",font="lucida 10 bold")
    l1_can=c.create_window(200,75,anchor="nw",window=l1)
    name_var = StringVar()
    e1=Entry(root,textvariable=name_var,width="32")
    e1_can=c.create_window(350,75,anchor="nw",window=e1)
    l2=Label(root,text="Enrollment No : ",font="lucida 10 bold")
    l2_can=c.create_window(200,125,anchor="nw",window=l2)
    venroll = StringVar()
    e2=Entry(root,textvariable=venroll,width="32")
    e2_can=c.create_window(350,125,anchor="nw",window=e2)
    l3=Label(root,text="Class",font="lucida 10 bold")
    l3_can=c.create_window(200,175,anchor="nw",window=l3)
    vyear = StringVar()
    vyear.set("1") # default value
    w = OptionMenu(root,vyear, "1", "2", "3","4","5","6","7","8")
    w_can=c.create_window(350,175,anchor="nw",window=w)
    l4=Label(root,text="Status",font="lucida 10 bold")
    l4_can=c.create_window(200,225,anchor="nw",window=l4)
    vstate = StringVar()
    vstate.set("") # default value
    w1 = OptionMenu(root,vstate,"Present","Absent")
    w1_can=c.create_window(350,225,anchor="nw",window=w1)
    l5=Label(root,text="Date",font="lucida 10 bold")
    l5_can=c.create_window(200,275,anchor="nw",window=l5)
    vdate = StringVar()
    e3=Entry(root,textvariable=vdate,width="32")
    e3_can=c.create_window(350,275,anchor="nw",window=e3)
    l8=Label(root,text="Parents Email Id : ",font="lucida 10 bold")
    l88_can=c.create_window(200,325,anchor="nw",window=l8)
    vemail = StringVar()
    e26=Entry(root,textvariable=vemail,width="32")
    e26_can=c.create_window(350,325,anchor="nw",window=e26)
    btn=Button(root,text="OK",bg="green",fg="white",width="15",font="lucida 10 bold",command=change)
    btn_can=c.create_window(200,400,anchor="nw",window=btn)
    btn2=Button(root,text="Back",bg="blue",fg="white",width="15",font="lucida 10 bold",command=back)
    btn2_can=c.create_window(400,400,anchor="nw",window=btn2)
    c.pack(fill="both",expand="True")
    root.mainloop()
  
