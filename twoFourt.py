#!/usr/bin/python 

#import module (another file seperated from main project) into file

#import volumes         #way 1 of importing 

#or import this way to not have to use . accessor method 
from volumes import * 

#to see what is included from volumes
#print(dir(volumes)) 

print(cube(2,5,8))
