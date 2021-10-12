from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os 



img_path_dir = "your image path"
files = os.listdir(img_path_dir)

# load img from file
for file in files:  
   img = cv2.imread(file, cv2.IMREAD_UNCHANGED) # no color change
   data = img_to_array(img)
   samples = expand_dims(data, 0)
   datagen = ImageDataGenerator(zoom_range=[3.0, 4.0])
   it = datagen.flow(samples, batch_size=1)
   i = 5
   pyplot.subplot(330 + 1 + i) 
   batch = it.next()
   image = batch[0].astype('uint8')
   pyplot.imshow(image)
   pyplot.show()

   head_tail = os.path.split(file) # file name frame1
   img_name = head_tail[1]
   print(img_name) # frame1
   cv2.imwrite("./zoom_out/"+img_name , image)