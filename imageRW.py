#!/usr/bin/env python
# coding: utf-8

# In[35]:


import numpy as np
import cv2

# Load an color image in grayscale
path = 'E:/'
img = cv2.imread(path+'IMG_5222.jpg',1)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(path+'new.jpg',img)

