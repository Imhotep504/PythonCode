#!/usr/bin/python 

#more adv. features ;) 

#shift cipher 

alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(s, shift = 3): 
   encrypt_str = ""
   for c in s: 
     index = alpha.index(c)
     shift_index = (index + shift) % len(alpha)
     encrypt_str += alpha[shift_index]
   return encrypt_str

#now try out for yourself 
print("all chars will be shifted by 3 or number you supply;)")
print(encrypt("helloworld"))

def decrypt(e, shift = 3): 
   decrypt_str = ""
   for c in e: 
     index = alpha.index(c)
     shift_index = (index - shift) % len(alpha)
     decrypt_str += alpha[shift_index]
   return decrypt_str

#now try out for yourself
print("all chars will be reversed by 3 or numbber you supply") 
print(decrypt("khoorzruog"))
