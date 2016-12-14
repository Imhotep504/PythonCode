#!/usr/bin/python 

#using import (for modules) 

import math

#or to be specific you can use from 
from math import pi      #only import constant pi 

#or to import everything 
#from math import *          #now dont have to prefix w/ math.blah

#use 'as' to rename (alias 
from math import factorial as f


print(math.pi)
print(math.cos(math.pi))

#using as below 
print(f(0))
print(f(2))
print(f(4))
print(f(6))
print(f(8))


