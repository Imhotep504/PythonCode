#!/usr/bin/python 

#user input dawgggggg 
#use raw_input for python 2.7 instead of just input ;)
#use str to cast ;) 

first_name = str(raw_input("Please enter in your first name ")) 
middle_ini = str(raw_input("Please enter in your middle name "))
last_name  = str(raw_input("Please enter in your last name ")) 

#capitalize just because we can 
first_name = first_name.capitalize()
middle_ini = middle_ini.capitalize()
last_name =   last_name.capitalize()

#now format to get specific output ;) 
name_format = "{first} {middle:.1s} {last}"
print(name_format.format(first=first_name,middle=middle_ini,last=last_name))

