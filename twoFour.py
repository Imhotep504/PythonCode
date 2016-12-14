#!/usr/bin/python 

#loops and conditionals 

alpha = 'abcdefghijklmnopqrxtuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowels = 'aeiouAEIOU'
my_string = "Packt publishing rocks!"

numbers = [1,2,3,4,5,6,7,8,9]

total = 0 

for x in numbers: 
	if x % 2 == 0: 
		total += x 
	print(total)

chars = []
for ch in my_string: 
	if ch not in vowels and ch in alpha:
	    chars.append(ch) 
consonants = ''.join(chars) 
print(consonants)
