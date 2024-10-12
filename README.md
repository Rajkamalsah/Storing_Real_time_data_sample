# Real-Time Data Fetching, Storing, and Processing

This project demonstrates how to fetch real-time data from a serial connection, store it in a MySQL database, and perform real-time processing. The project is divided into three modules: `x` for reading values, `y` for inserting values, and the main module for managing the processes.

## Features

- **Real-Time Data Fetching**: Read data from a serial connection.
- **Data Storage**: Store the fetched data in a MySQL database.
- **Real-Time Processing**: Process the data in real-time and trigger actions based on specific conditions.

## Tools and Technologies

- **Python**
- **MySQL**
- **Serial Communication**
- **Multiprocessing**

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/realtime-data-processing.git
    cd realtime-data-processing
    ```

2. Install the required libraries:
    ```bash
    pip install mysql-connector-python pyserial
    ```

3. Set up your MySQL database and update the connection details in the code.

## Usage

### Module `x` (Reading Values)

This module reads values from the MySQL database and processes them based on specific conditions.

```python
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
        
        a = 5  # give your conditions here. When you get the trigger condition, you should insert trigger signal into table
        if a == 5:
            sql2 = "SELECT computer_time_at_ir_value_inserting FROM ir_sensor ORDER BY computer_time_at_ir_value_inserting DESC LIMIT 20"
            mycursor.execute(sql2)

            myresult2 = mycursor.fetchall()
            
            arduino_time = myresult2[-1]
            accurate_time_when_trigger_start_given = datetime.now()  # current time noted when trigger signal given
            signal = 'camera_triggered'
            
            # inserting these values into camera trigger table
            sql = "INSERT INTO camera_trigger(accurate_time_when_trigger_start_given, arduino_time, output) VALUES (%s, %s, %s)"
            val = (accurate_time_when_trigger_start_given, arduino_time, signal)
            mycursor.execute(sql, val)
            
            # also inserting specific trigger time to experiment table 
            sql3 = "INSERT INTO experiment (actual_time_when_you_get_the_conditions, arduino_time_when_you_get_the_conditions) VALUES (%s, %s)"
            val3 = (accurate_time_when_trigger_start_given, arduino_time)  # note the comma

            # Execute the query
            mycursor.execute(sql3, val3)
           
            mydb.commit()
            break
