#!/usr/bin/python 

# T -> true, F -> false 
T = True
F = False 

if F or F: print("F or F") 
if F or T: print("F or T") 
if T or F: print("T or F")
if T or T: print("T or T") 
print("\n") 


if F and F: print("F or F") 
if F and T: print("F or T") 
if T and F: print("T or F")
if T and T: print("T or T") 

if not F: print("not F") 
if not T: print("not T") 
