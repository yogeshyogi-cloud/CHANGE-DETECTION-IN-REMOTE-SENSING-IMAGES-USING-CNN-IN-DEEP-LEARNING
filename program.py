#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

import matplotlib.pyplot as plt

import os
import cv2
#setting the path to the directory containing the pics
DATADIR="C:/datasets/traningdata"
CATEGORIES=['after','before']

for category in CATEGORIES:
path = os.path.join(DATADIR,category)
for img in os.listdir(path):
img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
plt.imshow(img_array, cmap="gray")

break

plt.show()
break
traning_data =[]
def create_traning_data():
for category in CATEGORIES:
path = os.path.join(DATADIR,category)
class_num = CATEGORIES.index(category)
for img in os.listdir(path):
try:

img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)

new_array = cv2.resize(img_array,(120,120))
plt.show()
traning_data.append([new_array, class_num])
except Exception as e:
print("Failed")
create_traning_data()
print(len(traning_data))
from PIL import Image, ImageChops
img1 = Image.open(r'C:\datasets\traningdata\before\01.jpg')
img2 = Image.open(r'C:\datasets\traningdata\after\02.jpg')
diff = ImageChops.difference(img1, img2)
diff.show()

