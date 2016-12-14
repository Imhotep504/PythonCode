#!/usr/bin/python 

#while loop 

index = 0 
names = ["josh", "patrick", "sammy", "jay"]

while index < len(names):
	name = names[index]
	print(name)
	index += 1

#second loop to iterate using while 
total = 0 
v = 1 

while v <= 10: 
	total += v 
	v += 1 
	print(total) 

print("Enter values totaling more than 20 to exit forever loop ;)") 
while True:
     a,b = int(raw_input("a = ")), int(raw_input("b = "))
     if a + b >= 20: 
	print("Now stopping loop, sentinel value hit")
	break
	
else: 
	print("so it should add up to 20 or more to exit") 
