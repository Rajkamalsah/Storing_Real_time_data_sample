# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:43:14 2024

@author: Raj
"""
from multiprocessing import Process
import x 
import y 

import time




#from here you start your experiment
if __name__ == '__main__':
    # Create two processes
    
    p1 = Process(target=y.insert_values)
    p2 = Process(target=x.read_values)
    

    # Start the processes
    
    p1.start()
    time.sleep(20)
    p2.start()
   

    
