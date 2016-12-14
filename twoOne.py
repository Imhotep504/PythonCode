#!/usr/bin/python

#in keyword and for loop 

one = "hello world" 
a = [4, 6, 9]

print(5 in a) 
print(4 in a)

#random for loop ;) 
for pee in [ 2, 3, 4, 56, 33, 32039, 230]:
	print(pee) 

print("now for another loop") 
odds = [1,3,5,7,9,11]
for ocd in odds: 
	print(ocd)

#now to get range/index of list 
print(range(len(odds)))
for index in range(len(odds)):
   print("Index: {:d}, odd number: {:d}".format(index, odds[index]))
