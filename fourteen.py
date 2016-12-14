#!/usr/bin/python 

#list slicing ;) 

#use range to generate a list 
a = list(range(0,12)) 
print(a) 

#now print first 6 in array 
print(a[0:6])

#or from 4th onward to end or list 
#or you can omit len and will auto reach the end ;) 
print(a[5:len(a)])
print(a[:])      #full array 

#now print every second object in array using step 
#default is 1 and hidden by default ;) 
print(a[::2])

#or index -> element # as well as step value 
print(a[0:8:2])

#just for fun lets use negative indices (just like in Ruby) 
print(a[-1])
print(a[-2]) 

#now use python canonical to reverse array 
print(a[::-1])



