import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the original and modified images
original_image_path = 'og.png'
modified_image_path = 'ogwithqr.png'

# Read the images in grayscale (black and white)
original = cv2.imread(original_image_path, cv2.IMREAD_GRAYSCALE)
modified = cv2.imread(modified_image_path, cv2.IMREAD_GRAYSCALE)

# Ensure both images are loaded properly
if original is None or modified is None:
    raise FileNotFoundError("One or both images not found. Please check the paths.")

# Step 1: Compute the initial absolute difference
difference = cv2.absdiff(original, modified)

# Step 2: Normalize the difference image
normalized = cv2.normalize(difference, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Save the normalized difference to the same folder as the script
output_folder = os.path.dirname(__file__)
normalized_output_path = os.path.join(output_folder, "normalized_difference.png")
cv2.imwrite(normalized_output_path, normalized)
print(f"Normalized difference saved to {normalized_output_path}")

# Adaptive histogram equalization function
def apply_clahe(image, clip_limit=2.0, tile_grid_size=(8, 8)):
    """
    Apply Contrast Limited Adaptive Histogram Equalization (CLAHE) to enhance the contrast.
    :param image: Input grayscale image.
    :param clip_limit: Threshold for contrast limiting.
    :param tile_grid_size: Size of the grid for histogram equalization.
    :return: Image after applying CLAHE.
    """
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    return clahe.apply(image)

# Iteratively enhance the normalized difference
iterations = 4
iterative_results = [normalized]
current_image = normalized

for i in range(iterations):
    # Compute the difference between the current image and a blurred version
    next_difference = cv2.absdiff(current_image, cv2.medianBlur(current_image, 3))
    # Normalize to maximize intensity range
    normalized_difference = cv2.normalize(next_difference, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    # Apply adaptive histogram equalization to enhance contrast
    enhanced_image = apply_clahe(normalized_difference, clip_limit=2.0, tile_grid_size=(8, 8))
    current_image = enhanced_image
    iterative_results.append(current_image)

# Display the results
plt.figure(figsize=(15, 10))

# Original Difference
plt.subplot(2, 3, 1)
plt.imshow(difference, cmap='gray')
plt.title('Difference Image')
plt.axis('off')

# Normalized Difference
plt.subplot(2, 3, 2)
plt.imshow(normalized, cmap='gray')
plt.title('Normalized Difference')
plt.axis('off')

# Iterative Results with CLAHE
for i in range(iterations):
    plt.subplot(2, 3, i + 3)
    plt.imshow(iterative_results[i], cmap='gray')
    plt.title(f'Iteration {i + 1}')
    plt.axis('off')

plt.tight_layout()
plt.show()

# Optionally, save the final resulting image
output_image_path = 'path_to_output_image/final_enhanced_qr_code.png'
cv2.imwrite(output_image_path, iterative_results[-1])
print("QR code enhancement complete. Check the output image.")
