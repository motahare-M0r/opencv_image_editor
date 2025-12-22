

import cv2
import numpy as np
import matplotlib.pyplot as plt 


# Read Image
img = cv2.imread('./img/Penguin.png')

img_resize = cv2.resize(img,(200,100))      
img_gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)




# Display
plt.figure(figsize=[8,5])
plt.subplot(131); plt.imshow(img[...,::-1]); plt.title(f'orginal {img.shape}')
plt.subplot(132); plt.imshow(img_resize[...,::-1]); plt.title(f'image resize {img_resize.shape}')
plt.subplot(133); plt.imshow(img_gray, cmap='gray'); plt.title(f'gray image  {img_gray.shape}')

plt.show()

cv2.imshow('image' , img)