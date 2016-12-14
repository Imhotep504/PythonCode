#!/usr/bin/python 

#more of PIL pillow manipulations w/ colors  LEGGO!!

#import modules of course 
from PIL import Image, ImageFilter, ImageEnhance 

egypt_img = Image.open("egypt.jpeg") 

#grayscale for black and white really lol 
grayscale = egypt_img.convert('L') 
grayscale.show() 

#now for edge detection (sort of outline of inside image 
edge_detection = egypt_img.filter(ImageFilter.FIND_EDGES)
edge_detecion.show() 

#now for contrast 
contrast = ImageEnhance.Contrast(egypt_img).enhance(2.5)
contrast.show() 

#and now for brightness 
bright = ImageEnhance.Brightness(egypt_img).enhance(4) 
bright.show() 
