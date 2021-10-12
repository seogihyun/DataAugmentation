import glob 
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os 
import imutils 


angle = [60, 120, 180, 240, 300]

img_path_dir = "your image path"
file_list = os.listdir(img_path_dir)

for i in sorted(file_list):
  image = cv2.imread(img_path_dir + i)
  for a in angle:
     rotated = imutils.rotate(image, a)
     head_tail = os.path.split(i) 
     img_name = head_tail[1]
     print(img_name)
     print(i)
     cv2.imwrite("저장할 경로" + "_rotation_" + str(a)+_img_name , rotated)

