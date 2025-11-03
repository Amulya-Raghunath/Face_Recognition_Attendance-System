# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 22:12:43 2021

@author: HP
"""

from tkinter import *
import tkinter.ttk as ttk
from datetime import datetime
import csv
def attend():
    root=Tk()
    root.title("View Attendance of today")
    width=500
    height=500
    sw=root.winfo_screenwidth()
    sh=root.winfo_screenheight()
    x=(sw/2)-(width/2)
    y=(sh/2)-(height/2)
    root.geometry("%dx%d+%d+%d" %(width,height,x,y))
    root.resizable(0,0)
    TM=Frame(root,width=400)
    TM.pack(side=TOP)
    scrollbarx=Scrollbar(TM,orient=HORIZONTAL)
    scrollbary=Scrollbar(TM,orient=VERTICAL)
    tree=ttk.Treeview(TM,columns=('roll_no','name','status'),height=300,selectmode="extended",yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT,fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=RIGHT,fill=X)
    tree.heading('roll_no',text='roll_no',anchor=W)
    tree.heading('name',text='name',anchor=W)
    tree.heading('status',text="status",anchor=W)
    tree.column('#0',stretch=NO,width=0)
    tree.column('#1',stretch=NO,width=100)
    tree.column('#2',stretch=NO,width=150)

    p1=datetime.date(datetime.now())
    p=str(datetime.date(datetime.now()))
    s=p1.strftime("%B,%Y")
    pr=0
    a=0
    count=0
    with open('attendance_report/'+s+'/Attendance_'+p+'.csv') as f:
        reader=csv.DictReader(f,delimiter=',')
        for row in reader:
            roll_no=row['roll_no']
            name=row['name']
            status=row['status']
            tree.insert("",0,values=(roll_no,name,status))
            count+=1

            if(row['status']=='Present'):
                pr=pr+1
            else:
                a+=1
        tree.insert("",7,values=("Total",count))
        tree.insert("",8,values=("No of Present",pr))
        tree.insert("",9,values=("No of Absentees",a))

    print("Present is ",pr)
    print("Absent is ",a)
    tree.pack()
    root.mainloop()

