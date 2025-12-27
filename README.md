# OpenCV Image Editor

A step-by-step image processing project built with **OpenCV** and **Python**, focusing on image enhancement techniques and preparing images for further computer vision tasks.

This project is developed incrementally in multiple phases, each introducing new image processing concepts.

---

## 🔧 Technologies
- Python
- OpenCV
- NumPy
- Matplotlib

---

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

This phase focuses on improving image quality, especially for **medical images, scans, and low-quality cameras**.

### Noise Reduction
The following denoising techniques are applied on grayscale images:

- **Gaussian Blur**  
  Suitable for reducing smooth Gaussian noise.

- **Median Blur**  
  Effective for removing impulse (salt-and-pepper) noise while preserving edges.

- **Bilateral Filter**  
  Reduces noise while preserving edges, commonly used in medical imaging.

### Sharpening
Sharpening is applied **after noise removal** to avoid amplifying noise.

- **Kernel-based Sharpening**  
  A convolution kernel is used to enhance edges.

- **Unsharp Masking**  
  Enhances structural details by combining the denoised image with a blurred version.


---


```python
Noise_Removal_and_Sharpening()
