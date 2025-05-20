#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


# Step 2: Load the image using imread() from cv2 module
image = cv2.imread('house image.jpg')  # Replace 'image.jpg' with your image path


# In[5]:


# Step 3: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# In[14]:


# Step 4: Sobel Edge Detection (Using Sobel operator)
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel edge detection in X direction
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel edge detection in Y direction
sobel_edge = cv2.magnitude(sobel_x, sobel_y)  # Combine X and Y Sobel results

     


# In[7]:


laplacian_edge = cv2.Laplacian(gray_image, cv2.CV_64F)  # Apply Laplacian operator


     


# In[8]:


# Step 5: Canny Edge Detection
canny_edge = cv2.Canny(gray_image, 100, 200)  # Canny edge detector with threshold values 100 and 200


# In[15]:


# Laplacian Edge Detector output
plt.subplot(2, 2, 2)
plt.imshow(laplacian_edge, cmap='gray')
plt.title("Laplacian Edge Detector")
plt.axis('off')

# Canny Edge Detector output
plt.subplot(2, 2, 3)
plt.imshow(canny_edge, cmap='gray')
plt.title("Canny Edge Detector")
plt.axis('off')

# Show the plots
plt.tight_layout()
plt.show()


# In[ ]:




