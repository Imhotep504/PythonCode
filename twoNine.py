#!/usr/bin/python 

#void vs return values ;) 

#reverse string input 
def reverse(s): 
   new_str = ""
   for i in range(len(s)):
     new_str += s[len(s) -i -1]
   return new_str 

print(reverse("1234"))
print(reverse("askd"))
print(reverse("Gunna"))

#now for the palindrome 
def is_palindrome(p): 
   for x in range(len(p)//2):       #// for integer division ;) 
      if p[x] != p[len(p) -x -1]:
	print("No you don't have a palindrome")         
        return      #to exit function 
   print("Yes you have a palindrome") 


print(is_palindrome("2"))
print(is_palindrome("abba"))
print(is_palindrome("121"))
print(is_palindrome("Hello"))

