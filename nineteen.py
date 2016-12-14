#!/usr/bin/python 

a,b = int(raw_input("a = ")), int(raw_input("b = " ))
if a % b == 0 or b % a == 0: 
	print("divisible") 
else: 
	print("Not evenly divisible") 

#test to ensure d is not zero 
c,d = int(raw_input("c = ")), int(raw_input("d = "))
if d != 0:
       print (c/d)

#now get two inputs and test if both names are equal if so print equal
print("Now enter in two names and see if they are the same")
name1 = raw_input("name1: ")
name2 = raw_input("name2: ")

if name1.lower() == name2.lower():
	print("so the names are equal after all")
else: 
	print("Sorry but those were not equal")
