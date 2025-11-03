#import module from tkinter for UI
from tkinter import *
from PIL import ImageTk,Image
#from playsound import playsound
import os
from datetime import datetime;
import mysql.connector;
import dataset_capture as dc
import database1 as db1
import face_training as ft
import face_recognition as fr
import Add_new as ad
import View  as vi
import delete as dt
import update as up
import Now as nw
def firstpage():
    root=Tk()
       

    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    mycursor = mydb.cursor()

    #sql="UPDATE Attend SET status='Absent' WHERE status='Present';"
    #mycursor.execute(sql);
    #mydb.commit();
    #print(mycursor.rowcount, "record inserted.")
    s = "update Attend SET date=current_date();"
    mycursor.execute(s);
    mydb.commit()
    #print(mycursor.rowcount, "record inserted.")
    #print("Database updated")
    #root.configure(background="white")

    #root.geometry("300x300")

    def function1():
        dc.dataset_capture()
    
    def function2():
        
        ft.training()

    def function3():
       

        fr.face()
    #playsound('sound.mp3')

    def function5():
        root.destroy()
        os.system("python login.py")
    
    def function6():
        root.destroy()
        ad.add_new()
    
    def viewL():
        root.destroy()
        vi.view()
        

    def attend():
        
        db1.database()
    
    def dete():
        root.destroy()
        dt.deleting()
        
    def updating():
        root.destroy()
        up.modify()
        
    def function7():
        nw.attend()

#stting title for the window
    root.title("FACIAL RECOGNITION BASED ATTENDANCE SYSTEM AND MANAGEMENT")
    #pic = Image.open("images\\wallpaper.png")
    #pic=pic.resize((768,512), Image.ANTIALIAS)
    c=Canvas(root,bg="blue",height=512,width=768)
    fn=PhotoImage(file="images\\wallpaper.png")
    c.create_image(0,0,image=fn,anchor="nw")
    #c.create_text(100,100,text="WELCOME TO THE FACIAL RECOGNITION ATTENDANCE SYSTEM ",font="lucida 10 bold")
    
#creating a text label
    l1=Label(root, text="WELCOME TO THE FACIAL RECOGNITION ATTENDANCE SYSTEM ",font="lucida 15 bold",fg="blue",bg="Orange",height=3)
    l1_canvas=c.create_window(50,10,anchor="nw",window=l1)
#creating first button
    photo5=PhotoImage(file=r"images\\create.png")
    btn1=Button(root,text="Create Face Dataset",image=photo5,compound=LEFT,font="lucida 10 bold",bg="SteelBlue1",fg='black',command=function1)
    btn_canvas=c.create_window(150,100,anchor="nw",window=btn1)
    
    photo6=PhotoImage(file=r"images\\train.png")
    btn2=Button(root,text="Train Face Dataset",image=photo6,compound=LEFT,font="lucida 10 bold",bg="SteelBlue2",fg='black',command=function2)
    btn2_can=c.create_window(150,140,anchor="nw",window=btn2)
    
    ph1=PhotoImage(file=r"images\\Set.png")
    btn3=Button(root,text="Recognize Face and Set Attendance",image=ph1,compound=LEFT,font="lucida 10 bold",bg="SteelBlue3",fg="black",command=function3)
    btn3_can=c.create_window(150,180,anchor="nw",window=btn3)
    
    pho=PhotoImage(file=r"images\\attendance.png")
    btn4=Button(root,text="Generate Attendance Sheet",image=pho,compound=LEFT,font="lucida 10 bold",bg="SteelBlue4",fg="black",command=attend)
    btn4_can=c.create_window(150,220,anchor="nw",window=btn4)
    
    photo=PhotoImage(file=r"images\\add.png")
    btn5=Button(root,text="Add",image=photo,compound=LEFT,bg="SkyBlue1",fg="black",font="lucida 10 bold",command=function6)
    btn5_can=c.create_window(150,260,anchor="nw",window=btn5)
    
    photo2=PhotoImage(file=r"images\\Search.png")
    #Button(root,text="Add new student",font=('times new roman',10),bg="SkyBlue1",fg="black",command=function6).grid(row=11,columnspan=2,pady="10")
    btn6=Button(root,text="View Details ",font="lucida 10 bold",compound=LEFT,image=photo2,bg="SkyBlue2",fg="black",command=viewL)
    btn6_can=c.create_window(150,300,anchor="nw",window=btn6)
    
    photo3=PhotoImage(file=r"images\\delete.png")
    btn7=Button(root,text="Delete ",font="lucida 10 bold",image=photo3,compound=LEFT,bg="SkyBlue3",fg="black",command=dete)
    btn7_can=c.create_window(150,340,anchor="nw",window=btn7)
    
    photo8=PhotoImage(file=r"images\\update.png")
    btn9=Button(root,text="Update ",font="lucida 10 bold",image=photo8,compound=LEFT,bg="SkyBlue3",fg="black",command=updating)
    btn9_can=c.create_window(150,380,anchor="nw",window=btn9)
    
    photo10=PhotoImage(file=r"images\\attend.png")
    btn10=Button(root,text="View Attendance of now",font="lucida 10 bold",image=photo10,compound=LEFT,bg="SkyBlue4",fg="black",command=function7)
    btn10_can=c.create_window(150,420,anchor="nw",window=btn10)
    
    photo4=PhotoImage(file=r"images\\exit.png")
    btn8=Button(root,text="Logout",font="lucida 10 bold",image=photo4,compound=LEFT,bg="SkyBlue4",fg="black",command=function5)
    btn8_can=c.create_window(150,460,anchor="nw",window=btn8)
    c.pack(fill="both",expand="True")
    root.mainloop()
