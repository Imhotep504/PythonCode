#!/usr/bin/python 

#formatting ;) 
# e - exponent b - binary o - octal  d - decimal 
# x - hexadecimal  f - floats   s - strings 

n = 11 
f = 3.14
s = "Gunna"

print("my number is {:d}".format(n))   #printed in decimal ;) 
print("my number is {:b}".format(n))   #printed in binary  ;) 

print("{:f}".format(f)) 
print("{:.2f}".format(f))     #number of decimal places 
print("{:15.2f}".format(f))   #padding + number of decimal places 
print("{:015.2f}".format(f))  #padding w/ 0's + number of decimal places 

#printing multiple
print("Now printing multiple ;)")
print("{0} {1} {2}".format(n,f,s))

#or do it another way here below 
print("just to seperate the other way")
print("{name} has {amt} of {fruit}".format(
	name = "Ayo", 
	amt = 17,
	fruit = "beans"
))
