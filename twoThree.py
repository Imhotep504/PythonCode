#!/usr/bin/python 

#iterables ;) 

list = [1,3,4,5,6]
tuple = (2,5,32,6,9)   #same as list although immutable ;) 
string1 = "Hello Gunna!"

print('__iter__' in dir(list))
print('__iter__' in dir(tuple))
print('__iter__' in dir(string1))


#essentially what a for loop is doing under the hood lol 

list_iterator = iter(list)

while True:
   try: 
      next_elem = next(list_iterator)
      print(next_elem)
   except StopIteration: 
      break
  
