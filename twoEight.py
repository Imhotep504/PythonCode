#!/usr/bin/python 

import datetime as dt

#regular function 
#def add(a,b,c): 
#	return a + b + c

#print(add(1,2,4))

#variadic function ;) 

def add_num(*numbers): 
 total = 0 
 for x in numbers:
    total += x 
 return total 

print(add_num(3,5,8,7))

def record_time(message, time = dt.datetime.now() ): 
   print("{:}, time: {:}".format(message, time))

record_time("It is morning") 
record_time("It is morning", "Election year 2016 ;(") 
