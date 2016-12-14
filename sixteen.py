#!/usr/bin/python 

#multiline entry 

tmp = """
(-40, -25) Super Cold
(-24, 0) Cold Dude 
(0, 32) Nippy 
(33, 65) Chilly 
(66, 90) Pretty warm
(91, 100) Summer Time! 
     """

#print to stdout 
print("Enter in the temp dude")
print(tmp) 

#cast input to int
t = int(raw_input())

if ( t < -25): 
	print("Super cold out")
if ( t > -25): 
	if (t < 0): 
		print("Its Cold dude") 
if ( t >= 0 ): 
	if (t <= 32): 
		print("Its really Nippy") 
if ( t >= 33): 
	if (t <= 65): 
		print("Its feeling chilly") 
if ( t >= 66): 
	if (t <= 90): 
		print("Its pretty warm out")
if ( t > 90): 
	print("It must be summer time") 
