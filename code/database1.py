# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 20:18:00 2021

@author: HP
"""

import mysql.connector
import os
from openpyxl import Workbook
import csv
from datetime import datetime
def database():
    p1=datetime.date(datetime.now())
    p=str(datetime.date(datetime.now()))

    s=p1.strftime("%B,%Y")
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="hanu123",database="student_database")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Attend")

    rows = mycursor.fetchall()
    if os.path.exists('attendance_report/'+s):
        with open('attendance_report/'+s+'/Attendance_'+p+'.csv', 'w') as f:
            a = csv.writer(f, delimiter=',')
            a.writerow(["name","roll_no","class","status","date"])  ## etc
            a.writerows(rows)
    else:
        os.mkdir('attendance_report/'+s)
        with open('attendance_report/'+s+'/Attendance_'+p+'.csv', 'w') as f:
            a = csv.writer(f, delimiter=',')
            a.writerow(["name","roll_no","class","status","date"])  ## etc
            a.writerows(rows)
database()