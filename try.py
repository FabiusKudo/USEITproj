import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the original and modified images
original_image_path = 'ogwithqr.png'
modified_image_path = 'image.png'
# Read the images in grayscale (black and white)
original = cv2.imread(original_image_path, cv2.IMREAD_GRAYSCALE)
modified = cv2.imread(modified_image_path, cv2.IMREAD_GRAYSCALE)
# Ensure both images are loaded properly
if original is None or modified is None:
    raise FileNotFoundError("One or both images not found. Please check the paths.")
# Compute the absolute difference between the original and modified images
difference = cv2.absdiff(original, modified)
# Apply a threshold to the difference to highlight the QR code
_, thresholded = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)
# Display the difference image and the thresholded image
plt.figure(figsize=(10, 5))
# Original vs Modified Difference
plt.subplot(1, 2, 1)
plt.imshow(difference, cmap='gray')
plt.title('Difference Image')
plt.axis('off')
# Thresholded Image (highlighted QR code)
plt.subplot(1, 2, 2)
plt.imshow(thresholded, cmap='gray')
plt.title('QR Code Highlighted')
plt.axis('off')
plt.show()
# Optionally, save the resulting image with highlighted QR code
output_image_path = 'path_to_output_image/highlighted_qr_code.png'
cv2.imwrite(output_image_path, thresholded)
print("QR code extraction complete. Check the output image.")
