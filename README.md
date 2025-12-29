# OpenCV Image Editor

A step-by-step image processing project built with **OpenCV** and **Python**, focusing on image enhancement, segmentation, and structural analysis as preparation for advanced computer vision tasks.

This project is developed incrementally in multiple phases, where each phase introduces new image processing concepts and techniques.

---

## 🔧 Technologies
- Python
- OpenCV
- NumPy
- Matplotlib

---

## Phase 1 – Image Enhancement Basics (v0.1)

This phase introduces fundamental image enhancement operations.

### Implemented Features
- Image loading and resizing
- Color space conversion (BGR → RGB → Grayscale)
- Brightness adjustment (addition / subtraction)
- Contrast adjustment (multiplication)
- Basic smoothing filters:
  - Gaussian Blur
  - Median Blur

### Purpose
- Understand pixel-wise operations
- Learn how brightness and contrast affect image appearance
- Get familiar with basic smoothing techniques

---

## Phase 2 – Noise Removal & Sharpening (v0.2)

This phase focuses on improving image quality, especially for medical images, scanned documents, and low-quality cameras.

### Noise Reduction Techniques
- **Gaussian Blur**  
  Reduces smooth Gaussian noise.
- **Median Blur**  
  Removes salt-and-pepper noise while preserving edges.
- **Bilateral Filter**  
  Reduces noise while preserving edges.

### Sharpening Techniques
- **Kernel-based Sharpening**
- **Unsharp Masking**

### Purpose
- Improve image clarity
- Reduce noise without destroying edges
- Enhance structural details

---

## Phase 3 – Thresholding & Binarization (v0.3)

This phase introduces image segmentation fundamentals using thresholding techniques.

### Implemented Techniques
- Global Thresholding
- Adaptive Thresholding (Mean method)
- Otsu’s Thresholding
- Binary Inversion

### Morphological Operations
- Closing (fill small holes and gaps)
- Opening (remove small noise)

### Purpose
- Convert grayscale images into binary representations
- Separate foreground from background
- Prepare images for structural analysis

---

## Phase 4 – Edge & Structure Detection (v0.4)

This phase focuses on extracting edges and structural information from images.

### Processing Pipeline
- Grayscale conversion
- Noise reduction using Median Blur
- Edge detection using Canny
- Morphological refinement:
  - Closing
  - Opening

### Purpose
- Extract meaningful edges
- Improve edge continuity
- Generate structural representations for higher-level vision tasks

---

## Project Design

The project is designed incrementally, where each phase builds on the previous one:

- Phase 1: Image enhancement
- Phase 2: Noise removal and sharpening
- Phase 3: Thresholding and binarization
- Phase 4: Edge and structure detection

This modular design allows easy extension toward:
- Contour detection
- Shape analysis
- Object segmentation
- Document and map processing

---
