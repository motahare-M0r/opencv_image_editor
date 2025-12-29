

import cv2
import numpy as np
import matplotlib.pyplot as plt 




def base(img_path):
    
    # Read Image
    img = cv2.imread(img_path)

    img_resize = cv2.resize(img,(200,100))      
    img_gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)


    # Display
    plt.figure(figsize=[8,5])
    plt.subplot(131); plt.imshow(img[...,::-1]); plt.title(f'original {img.shape}')
    plt.subplot(132); plt.imshow(img_resize[...,::-1]); plt.title(f'image resize {img_resize.shape}')
    plt.subplot(133); plt.imshow(img_gray, cmap='gray'); plt.title(f'gray image  {img_gray.shape}')

    plt.show()

    cv2.imshow('image' , img)



# ===== Phase 1: Basic Enhancement =====
def Image_Enhancement_Basics(img_path):

    # Read Image
    img_bgr = cv2.imread(img_path) 
    img_rgb = cv2.cvtColor(img_bgr , cv2.COLOR_BGR2RGB)


    # Addition or Brightness
    matrix_brightness = np.ones(img_rgb.shape , dtype='uint8') * 80

    img_brighter = cv2.add(img_rgb , matrix_brightness)
    img_darker = cv2.subtract(img_rgb , matrix_brightness)



    # Multiplication or Contrast
    matrix_contrast_lower = np.ones(img_rgb.shape) * 0.6
    matrix_contrast_higher = np.ones(img_rgb.shape) * 1.5

    img_contrast_lower = np.uint8(cv2.multiply(np.float64(img_rgb) , matrix_contrast_lower))
    img_contrast_higher = np.uint8(np.clip(cv2.multiply(np.float64(img_rgb) , matrix_contrast_higher), 0 , 255))



    # Gaussian Blur / Median Blur
    img_Gaussian_Blur = cv2.GaussianBlur(img_rgb,(5,5),0) 
    img_Median_Blur =  cv2.medianBlur(img_rgb,5)





    # Display
    plt.figure(figsize=[10,10])

    plt.subplot(331); plt.imshow(img_darker , cmap='gray'); plt.title('Darker')
    plt.subplot(332); plt.imshow(img_rgb); plt.title('Original')
    plt.subplot(333); plt.imshow(img_brighter , cmap='gray'); plt.title('Brighter')

    plt.subplot(334); plt.imshow(img_contrast_lower); plt.title('Lower Contrast')
    plt.subplot(335); plt.imshow(img_rgb); plt.title('Original')
    plt.subplot(336); plt.imshow(img_contrast_higher); plt.title('Higher Contrast')

    plt.subplot(337); plt.imshow(img_Gaussian_Blur); plt.title('Gaussian Blur')
    plt.subplot(338); plt.imshow(img_rgb); plt.title('Original')
    plt.subplot(339); plt.imshow(img_Median_Blur); plt.title('Median Blur')



    plt.show()
    
# brightness, contrast, blur


# ===== Phase 2: Denoise & Sharpen =====
def Noise_Removal_and_Sharpening():

    img_bgr = cv2.imread('./img/mri.png') 
    img_gray = cv2.cvtColor(img_bgr , cv2.COLOR_BGR2GRAY)


    # ========== Part 1: Noise Removal ===========
    gaussian = cv2.GaussianBlur(img_gray , (5,5) , 0)
    median = cv2.medianBlur(img_gray , 5)
    bilateral = cv2.bilateralFilter(img_gray , 9 , 100 , 100)


    # ========== Part 2: Sharpening ===========
    kernel = np.array([[0 , -1 , 0],
                       [-1 , 5 , -1],
                       [0 , -1 , 0]])
    
    
    sharpen = cv2.filter2D(median, -1 , kernel)
    unSharpMask = cv2.addWeighted(median , 1.5 , gaussian , -0.5 , 0)




    # Display
    plt.figure(figsize=[15,8])

    plt.subplot(231); plt.imshow(img_gray , cmap='gray'); plt.title('Original')
    plt.subplot(232); plt.imshow(gaussian , cmap='gray'); plt.title('GaussianBlur')
    plt.subplot(233); plt.imshow(median , cmap='gray'); plt.title('medianBlur')
    plt.subplot(234); plt.imshow(bilateral , cmap='gray'); plt.title('BilateralFilter')
    plt.subplot(235); plt.imshow(sharpen , cmap='gray'); plt.title('Sharpening')
    plt.subplot(236); plt.imshow(unSharpMask , cmap='gray'); plt.title('unSharp Mask')

    plt.show()


# ===== Phase 3: Thresholding & Binarization =====
def Thresholding_and_Binarization():

    img = cv2.imread('./img/paper1.jpg' , 0)
    

    _ , thresh_100 = cv2.threshold(img , 100 , 255 , cv2.THRESH_BINARY)
    
    thresh_adp = cv2.adaptiveThreshold(img , 255 , cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY , 11 , 14 )

    _ , thresh_OTSU = cv2.threshold(img , 0 , 255 , cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _ , thresh_Invert = cv2.threshold(img , 120 , 255 , cv2.THRESH_BINARY_INV)


    # Morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    closed = cv2.morphologyEx(thresh_100 , cv2.MORPH_CLOSE , kernel)
    opened = cv2.morphologyEx(thresh_adp , cv2.MORPH_OPEN , kernel)

    

    # Display
    plt.figure(figsize=[8,6])

    plt.subplot(241); plt.imshow(img , cmap='gray'); plt.title('Original')
    plt.subplot(242); plt.imshow(thresh_100 , cmap='gray'); plt.title('Thresholding_100')
    plt.subplot(243); plt.imshow(thresh_adp , cmap='gray'); plt.title('AdaptiveThreshold')

    plt.subplot(244); plt.imshow(thresh_OTSU , cmap='gray'); plt.title('OTSU')
    plt.subplot(245); plt.imshow(thresh_Invert , cmap='gray'); plt.title('Invert')

    plt.subplot(246); plt.imshow(closed , cmap='gray'); plt.title('Morphology_closed')
    plt.subplot(247); plt.imshow(opened , cmap='gray'); plt.title('Morphology_opened')



    plt.show()


# ===== Phase 4: Edge & Structure Detection =====
def Edge_and_Structure_Detection(img_path):

    img = cv2.imread(img_path)

    img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)


    # First Denoise
    median = cv2.medianBlur(img_gray , 5 )

    # Detection with Canny
    canny = cv2.Canny(median , 50 , 150)


    # Morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    closed = cv2.morphologyEx(canny , cv2.MORPH_CLOSE , kernel)
    opened = cv2.morphologyEx(closed , cv2.MORPH_OPEN , kernel)



    # Display 
    plt.figure(figsize=[6 , 5])

    plt.subplot(221); plt.imshow(img_gray , cmap='gray'); plt.title('Original')
    plt.subplot(222); plt.imshow(canny , cmap='gray'); plt.title('Canny')
    plt.subplot(223); plt.imshow(closed , cmap='gray'); plt.title('closing')
    plt.subplot(224); plt.imshow(opened , cmap='gray'); plt.title('opening')


    plt.show()


image_path = './img/Penguin.png'

# Result

#base()
#Image_Enhancement_Basics(image_path)
#Noise_Removal_and_Sharpening()
Thresholding_and_Binarization()
#Edge_and_Structure_Detection(image_path)