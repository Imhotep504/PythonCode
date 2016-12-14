#!/usr/bin/python 

pre = " IM a GOD " 
suf = "and I MANIFEST what I Want" 

totl = pre + suf 
#print(totl) 

totl = totl * 2 
totl = totl.replace("a","A",1)     # 1 to only replace once ;) 
print(totl)

print(totl.count("I"))
