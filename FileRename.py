#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import cv2
cv2.__version__


# In[28]:


path = 'H:\Final year project\experiemtn/'
dirs = os.listdir(path)
for items in dirs:
    s=list(items)
    s[0]='0'
    tm="".join(s)#new_name
    os.rename(path+items, path+tm) 
    #print(type(tm))


# In[ ]:




