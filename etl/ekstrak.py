import numpy as np
import cv2
from skimage.feature import hog
from skimage.color import rgb2gray

def preprocess_data(image_bytes):
    # Mengonversi byte menjadi array NumPy
    image = np.frombuffer(image_bytes, dtype=np.uint8)

    # Decode gambar
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    # Konversi gambar ke grayscale
    gray_image = rgb2gray(image)

    # Periksa apakah gambar valid
    if gray_image is None:
        raise ValueError("Gambar tidak dapat dibaca.")
    
    # Ekstraksi fitur HOG
    fd = extract_hog_features(gray_image)
    
    return fd.reshape(1,-1)

def extract_hog_features(image):
    # Ekstraksi fitur HOG
    hog_features, hog_image = hog(image, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True, block_norm='L2-Hys')
    return hog_features
