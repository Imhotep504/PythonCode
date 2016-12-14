#!/usr/bin/python 

al1 = ["a", "f", "b", "e", "d"]
al2 = ["g", "i", "h"]
al3 = "jklmnopqrstuvwxyz"

al1.sort()
al2.sort() 

print(al1)
print(al2)

#insert missing c letter for sorted list 
al1.insert(2,"c") 

print(al1) 

#now concatenate the list together as if a string
print("Now to list together as if a string") 
al1 = ''.join(al1) 
al2 = ''.join(al2)

print(al1) 

#print("or with random symbol in between") 
#al1 = '->'.join(al1)
#print(al1)


alphabet = al1 + al2 + al3 

print("Now the full alphabet") 
print(alphabet) 





