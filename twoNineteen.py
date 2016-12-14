#!/usr/bin/python 

#custom manipulation (negating) 

from PIL import Image 

egypt_img = Image.open("egypt.jpeg") 
egypt_img.show() 

#w and h to loop thru all pixels ;) 
width, height = egypt_img.size 

for x in range(width): 
   for y in range(height): 

     pixel_coordinate = (x,y)   #.png images have 4 channels (alpha) ;) 
     r, g, b = egypt_img.getpixel(pixel_coordinate) 

     negative_color = (255 -r, 255 - g, 255 - b) 
     egypt_img.putpixel( pixel_coordinate, negative_color )

egypt_img.show() 
