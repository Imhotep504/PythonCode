#!/usr/bin/python 

#import for system exit 
import sys 

#prompt user for equation 
print("Enter in your equation to be calculated and spit out back at you") 

#create vars to accept values and operand from console 
line = raw_input() 
split = line.split()     #just like in Ruby 

left = int(split[0])
op = split[1]
right = int(split[2]) 

#place holder 
val = 0 

if op == '+':
	val = left + right
elif op == '-': 
	val = left - right 
elif op == '*': 
	val = left * right 
elif op == '/': 
	if right == 0: 
		print("Cant divide by zero Sunny ;)") 
		sys.exit()
                val = left / right 
else: 
    print("not sure wise guy of the operator: {operator}".format(operator=op))
    sys.exit()


#now print to stdout 
print("{line_expr} = {value:.2f}".format(line_expr=line, value=val)) 
