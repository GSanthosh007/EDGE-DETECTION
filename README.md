# EDGE-DETECTION
## Aim:
To perform edge detection using Sobel, Laplacian, and Canny edge detectors.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import all the necessary modules for the program.

### Step2:
Load a image using imread() from cv2 module.

### Step3:
Convert the image to grayscale

### Step4:
Using Sobel operator from cv2,detect the edges of the image.

### Step5:

Using Laplacian operator from cv2,detect the edges of the image and Using Canny operator from cv2,detect the edges of the image.

##Program:

```
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Step 2: Load the image using imread() from cv2 module
image = cv2.imread('house image.jpg')  # Replace 'image.jpg' with your image path
# Step 3: Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Step 4: Sobel Edge Detection (Using Sobel operator)
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel edge detection in X direction
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel edge detection in Y direction
sobel_edge = cv2.magnitude(sobel_x, sobel_y)  # Combine X and Y Sobel results
laplacian_edge = cv2.Laplacian(gray_image, cv2.CV_64F)  # Apply Laplacian operator
# Step 5: Canny Edge Detection
canny_edge = cv2.Canny(gray_image, 100, 200)  # Canny edge detector with threshold values 100 and 200

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

```

## Output:
### SOBEL EDGE DETECTOR
![Screenshot 2025-05-20 114215](https://github.com/user-attachments/assets/bb1c21ea-84de-4a6f-bb0f-5fb3d0732130)

### LAPLACIAN EDGE DETECTOR
![Screenshot 2025-05-20 114222](https://github.com/user-attachments/assets/03c80806-3f80-4d7c-af03-04233c5ea5a6)


### CANNY EDGE DETECTOR
![Screenshot 2025-05-20 114233](https://github.com/user-attachments/assets/f880560f-60d6-45ce-b1b4-968161639dd3)

## Result:
Thus the edges are detected using Sobel, Laplacian, and Canny edge detectors.
