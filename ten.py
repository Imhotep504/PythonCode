#!/usr/bin/python
#appending

alpha = ["a", "b", "d", "f"]
alpha.append("G")

#same way again 
alpha = alpha + ["T","C"]

#print list (array) 
print(alpha)

#print index as well 
G_index = alpha.index("G") 
print("G index is actually:" + str(G_index))

#now delete char at index ;) 
del alpha[G_index]
print(alpha) 

#or use remove to get index and remove in one step :)
alpha.remove("a")
print(alpha) 
