'''
Producer-Consumer Pattern Using Lock & Condition Variables
'''

import threading
import time
import random

BUFFER_SIZE=5
buffer=[]
lock=threading.Lock()
not_full=threading.Condition(lock)  # producers wait here
not_empty=threading.Condition(lock) # consumers wait here

def producer(name:str, items:int):
    pass

def consumer(name:str, items:int):
    pass

if __name__=="__main__":
    TOTAL_ITEMS=8
    threads=[
        
    ]

