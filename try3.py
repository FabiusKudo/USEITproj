import cv2
import numpy as np
import matplotlib.pyplot as plt

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

# Function to adjust brightness and contrast
def adjust_brightness_contrast(image, alpha=1.2, beta=20):
    """
    Adjusts brightness and contrast of an image.
    :param image: Input image (grayscale).
    :param alpha: Contrast multiplier (>1 increases contrast).
    :param beta: Brightness increment (positive values increase brightness).
    :return: Brightness and contrast adjusted image.
    """
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Iteratively enhance the normalized difference with brightness and contrast adjustment
iterations = 4
iterative_results = [normalized]
current_image = normalized

for i in range(iterations):
    # Normalize the difference between the current image and its blurred version
    next_difference = cv2.absdiff(current_image, cv2.medianBlur(current_image, 3))
    # Normalize again to bring intensities to full range
    normalized_difference = cv2.normalize(next_difference, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    # Adjust brightness and contrast
    enhanced_image = adjust_brightness_contrast(normalized_difference, alpha=1.5, beta=30)
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

# Iterative Results with Brightness and Contrast Adjustment
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
