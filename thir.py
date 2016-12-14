#!/usr/bin/python

#matrix's  (matrices) 
#imports below 
from pprint import pprint as pretty_print

#second imports 
from copy import copy, deepcopy

#2-d array 
nums_2d = [
	[1,2,3,4,5,6,7,],
	[8,9,10,11,12.13,14,15],
	[16,17,18,19,20,21,22]
]

#inital print 
print("Regular printing") 
print(nums_2d) 

print("Pretty printing now") 
pretty_print(nums_2d)

#now to change a random element [2][1]
nums_2d[2][1] = -5
nums_2d[2][2] = -5

print("New Matrix =>")
pretty_print(nums_2d)  

#now a 2-d array from a 1-D array
#use copy otherwise when manipulating elements you will change 
#each associated valued for each array -> ex. [0][0] A -> F does 
#so for all three rows :(   so use copy for 1-D + deepcopy for multi-D
letters = ["A", "B", "C", "D", "E"]
letters_2d = [ copy(letters), copy(letters), copy(letters)]

#now print out to stdout 
print("Now printing new 1-d => 2-d array")
pretty_print(letters_2d)


letters_2d[0][0] = 'Y'
print("now printing out new array with changed element ;)")
pretty_print(letters_2d) 
