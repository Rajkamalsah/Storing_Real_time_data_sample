# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:02:54 2024

@author: Raj
"""
import serial
import mysql.connector
import time
from datetime import datetime

def read_values():
    # establish a serial connection
    #ser = serial.Serial('COM3', 9600)

    # establish a MySQL connection
    mydb = mysql.connector.connect(
      host='a',user='b',password='',database='c'
    )

    mycursor = mydb.cursor()
    while True:
        time.sleep(0.1)
        sql1 = "SELECT irValue FROM ir_sensor ORDER BY computer_time_at_ir_value_inserting DESC LIMIT 20"
        mycursor.execute(sql1)

        myresult = mycursor.fetchall()
        #print(myresult)
        
        a=5  #give your conditions here.when you get the trigger condition you should insert trigger signal into table
        if a==5:
            
            sql2 = "SELECT computer_time_at_ir_value_inserting FROM ir_sensor ORDER BY computer_time_at_ir_value_inserting DESC LIMIT 20"
            mycursor.execute(sql2)

            myresult2 = mycursor.fetchall()
            
            arduino_time=myresult2[-1][0]
            accurate_time_when_trigger_start_given= datetime.now()      #current time noted when trigger signal given
            signal='camera_triggered'
            
            #inserting thsese values into camera trigger table
            sql = "INSERT INTO camera_trigger(accurate_time_when_trigger_start_given,arduino_time,output) VALUES (%s, %s,%s)"
            val = (accurate_time_when_trigger_start_given,arduino_time, signal)
            mycursor.execute(sql, val)
            

            
            
            #also inserting specific trigger time to experiment table 
            sql3="INSERT INTO experiment (actual_time_when_you_get_the_conditions,arduino_time_when_you_get_the_conditions) VALUES (%s,%s)"
            
            val3 = (accurate_time_when_trigger_start_given,arduino_time,)  # note the comma

            # Execute the query
            mycursor.execute(sql3, val3)
           
            mydb.commit()
            break
    
