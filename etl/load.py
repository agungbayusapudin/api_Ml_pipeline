from flask import Flask, request, jsonify
from PIL import Image
import cv2
import io
import numpy as np

def load_data(file_bytes):
    
    # Ubah byte array menjadi array NumPy
    np_array = np.frombuffer(file_bytes, np.uint8)

    # Decode gambar menggunakan OpenCV
    image = cv2.imdecode(np_array, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Gambar tidak valid atau tidak dapat dibaca.")
    
    # Resize gambar ke ukuran sesuai dengan model
    resized_image = cv2.resize(image, (98, 98))

    # Crop gambar dengan margin 15
    cropped_image = crop_image(resized_image, 15)

    # Encode gambar ke format JPEG
    _, encoded_image = cv2.imencode('.jpg', cropped_image)
    image_bytes = encoded_image.tobytes()

    return image_bytes


def crop_image(image_path, margin):
    # Baca gambar
    image = image_path

    # Dapatkan dimensi gambar
    height, width = image.shape[:3]

    # Tentukan koordinat untuk cropping
    left = margin
    right = width - margin
    top = margin
    bottom = height - margin

    # Potong gambar
    cropped_image = image[top:bottom, left:right]

    return cropped_image