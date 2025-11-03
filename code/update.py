from tkinter import *
import os
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import os
import mysql.connector
import Repage as fp
def modify():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    mycursor = mydb.cursor()
    def update():
        roll=venroll.get()
        data=vdata.get()
        state=vstate.get()
        if(roll=="" or data==""):
            tmsg.showinfo("Empty","Fill the field!!!")
        else:
            if(state=="Name"):
                sql="UPDATE Attend SET name= %s where roll_no = %s"
                values=(data,roll)
                mycursor.execute(sql,values)
                mydb.commit()
                tmsg.showinfo("Done","Updated done!!!")
                view()
                
                
            else:
                sql="UPDATE Attend SET class= %s where roll_no = %s"
                values=(data,roll)
                mycursor.execute(sql,values)
                mydb.commit()
                tmsg.showinfo("Done","Updated done!!!")
                view()
    
    def view():
        roll=venroll.get()
        mycursor.execute("Select * from Attend")
        myresult = mycursor.fetchall()
        mydb.commit()
        for r in myresult:
            if(roll==r[1]):
                l0=Label(f2,text="Updated data",font="lucida 10 bold").grid(column=0,row=5,pady="4")
                l2=Label(f2,text="Name: ",font="lucida 10 bold").grid(column=0,row=6,pady="4")
                a2=Label(f2,text=r[0],font="lucida 10 bold").grid(column=1,row=6,pady="4")
                l3=Label(f2,text="Roll_no: ",font="lucida 10 bold").grid(column=0,row=7,pady="4")
                a3=Label(f2,text=r[1],font="lucida 10 bold").grid(column=1,row=7,pady="4")
                l4=Label(f2,text="Class: ",font="lucida 10 bold").grid(column=0,row=8,pady="4")
                a4=Label(f2,text=r[2],font="lucida 10 bold").grid(column=1,row=8,pady="4")
                
    def back():
        root.destroy()
        fp.firstpage()
        
                

            
    
    root=Tk()
    root.title("UPDATE VALUES")
    root.geometry("150x200")
    root.maxsize(580,550)
    root.minsize(580,550)
    photo = ImageTk.PhotoImage(file=r"images\register.png")
    label=Label(image=photo)
    f2=Frame(label)
    l0=Label(f2,text="Update details",bg="orange",fg="blue",font="lucida 10 bold",width="35",pady="4").grid(columnspan=3,row=0,pady="15")
    l1=Label(f2,text="Roll_no: ",font="lucida 10 bold").grid(column=0,row=1,pady="4")
    venroll = StringVar()
    e1=Entry(f2,textvariable=venroll,width="32").grid(column=1,row=1)
    l3=Label(f2,text="Field you want to modify: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")
    vstate = StringVar()
    vstate.set("Name") # default value
    w1 = OptionMenu(f2,vstate,"Name","Class")
    w1.grid(column=1,row=2)
    l5=Label(f2,text="Enter the modified data: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")
    vdata = StringVar()
    e1=Entry(f2,textvariable=vdata,width="32").grid(column=1,row=3)
    btn=Button(f2,text="Update",bg="green",fg="white",width="10",font="lucida 10 bold",command=update)
    btn.grid(columnspan=3,row=4,pady="20")
    btn=Button(f2,text="Back",bg="blue",fg="white",width="10",font="lucida 10 bold",command=back)
    btn.grid(columnspan=1,row=4,pady="20")
    label.pack(ipadx="100",fill=BOTH)
    f2.pack(pady="50")
    root.mainloop()

