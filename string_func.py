#!/usr/bin/python 

#file to be used for module testing ;) 

def first_half(s): 
   return s[:len(s)/2]

def last_half(s): 
   return s[len(s)/2:]


if __name__ == '__main__':
   print("testing string functions") 
   assert first_half("abcd") == "ab", "First half is failing"
   assert  last_half("abcd") == "cd", "Last half is failing" 

