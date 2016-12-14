#!/usr/bin/python 

#image manipulation 

#define function to resize image and also rename as not to replace 

def resize_images(image_names, new_size = (200, 200)): 
   for image_name in image_names: 
      img = Image.open(image_name)
      img = resize(new_size) 
      img = ("resized"+image_name)

images = ["egypt.jpeg", "random.jpeg", "listed.jpeg"]

#now run function on images 
resize_images(images) 

#now crop and image x1, y1, x2, y2 
random_img = Image.open("random.jpeg") 
random_img.show() 

random_img = random_img.crop( (100, 100, 300, 300) ) 
random_img.show() 

#or rotate ;)   90 degrees for example 
random_img = random_img.rotate(90) 
random_img.show() 
