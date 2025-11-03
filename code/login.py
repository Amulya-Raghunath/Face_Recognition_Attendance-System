from PIL import Image, ImageTk
from tkinter import *
import tkinter.messagebox as tmsg
import mysql.connector
import Auth as au
import register as re
#import View as vi
import os


global root
root=Tk()
def Login():
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM login")
    #user1='Jaanu'
    #passw='123457'
    lid1=lid.get()
    lpass1=lpass.get()
        #print(lid.get(),lpass.get())
    
    rows = mycursor.fetchall()
    if(lid1=='' or lpass1==''):
        tmsg.showwarning('Please enter','ENTER EVERYTHING')
    else:
        for r in rows:
        
            #root.destroy()
            #os.system("python login.py")
            if(lid1==r[0] and lpass1==r[1]):
                flag=1
                break
            else:
                flag=0
            
    if flag==1:
        tmsg.showinfo('Success','Login Successful')
                
        root.destroy()
        au.auth()
        
    else:
        tmsg.showwarning('Not found','User credientials invalid')
            
    
def Register():
    print("Successful")
    root.destroy()
    re.register()

def student():
    root.destroy()
    os.system("python Student.py")
    
def ending():
    root.destroy()
    
global lid,lpass
# creating fixed geometry of the 
# tkinter window with dimensions 150x200 
root.geometry("150x200")
root.maxsize(580,550)
root.minsize(580,550)

#providing a title
root.title("FACULTY PORTAL")
#pic = Image.open("images\\wallpaper.png")
#pic=pic.resize((768,512), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(file=r"images\\login.png")

l_login=Label(image=photo)
f_login=Frame(l_login,pady="20",padx="20") #cretaing a Frame which can expand according to the size of the window
mainmenu=Menu(l_login)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="Student Portal",command=student)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="Student", menu=m1)
lb0 =Label(f_login,text="FACULTY PORTAL",bg="orange",fg="blue",font="lucida 10 bold",width="35",pady="4").grid(columnspan=3,row=0,pady="15")
lb1 =Label(f_login,text="Enter ID: ",font="lucida 10 bold").grid(column=0,row=2,pady="4")

lid =StringVar()
e1 =Entry(f_login,textvariable=lid,width="28").grid(column=1,row=2)
lb2 =Label(f_login,text="Enter Password: ",font="lucida 10 bold").grid(column=0,row=3,pady="4")

lpass=StringVar()
e2=Entry(f_login,textvariable=lpass,show="*",width="28").grid(column=1,row=3)
btn=Button(f_login,text="login",bg="green",fg="white",width="10",font="lucida 10 bold",command=Login)
btn.grid(column=0,row=5,pady="10")


btn2=Button(f_login,text="Register",bg="blue",fg="white",width="10",font="Lucida 10 bold",command=Register)
btn2.grid(column=1,row=5,pady="10")
btn3=Button(f_login,text="Close",bg="red",fg="white",width="10",font="Lucida 10 bold",command=ending)
btn3.grid(column=2,row=5,pady="10")
l_login.pack(ipadx="100",fill=BOTH)
f_login.pack(pady="165")
root.mainloop()