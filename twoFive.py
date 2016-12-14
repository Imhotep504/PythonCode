#!/usr/bin/python 

#prime number checker 

n = int(raw_input("n = ")) 

divisors = []    # list 

for divisor in range(2,n): 
	if n % divisor == 0: 
		divisors.append(divisor) 

if len(divisors) == 0:
   print("{:d} is prime!".format(n))
else: 
   print("{:d} is not prime because {:} divide {:d}".format(n, str(divisors), n)), 
