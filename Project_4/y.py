# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:04:19 2024

@author: Raj
"""

import serial
import mysql.connector
from multiprocessing import Process
from datetime import datetime


def insert_values():
    # establish a serial connection
    ser = serial.Serial('COM4', 9600)

    # establish a MySQL connection
    mydb = mysql.connector.connect(
      host='a',user='b',password='',database='c'
    )

    mycursor = mydb.cursor()
    
    #this is the start point of the experiment.you should send this time to experiment table
    start_time_of_experiment=datetime.now()
    #also inserting these times bof before and after trigger to experiment table 
    sql3="INSERT INTO experiment ( start_time_of_experiment) VALUES (%s)"
    # The value you want to insert
    # The value you want to insert
    val3 = (start_time_of_experiment,)  # note the comma

    # Execute the query
    mycursor.execute(sql3, val3)
   
    mydb.commit()
 
    
    
    
    
    while True:
      if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()  # read a '\n' terminated line
        
        #print(line)
        # Split the string and extract the sensor value and time
        parts = line.split(',')
        sensor_value = int(parts[0].split(':')[1].strip())
        ir_times = int(parts[1].split(':')[1].strip())
        

        
        #insert_table(time,sensor_value)
        computer_time_at_ir_value_inserting_1=datetime.now()
        

        sql = "INSERT INTO ir_sensor (computer_time_at_ir_value_inserting,ir_time,  irValue) VALUES (%s,%s, %s)"
        val = (computer_time_at_ir_value_inserting_1,ir_times, sensor_value)
        mycursor.execute(sql, val)

        mydb.commit()
        
        
