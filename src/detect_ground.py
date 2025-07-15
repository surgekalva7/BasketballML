import cv2
import numpy as np

def detect_ground_position(image):
    # Convert to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define color range for the floor (adjust based on your floor color)
    lower_bound = np.array([20, 50, 50])  # Example for wooden floor
    upper_bound = np.array([40, 255, 255])
    
    # Create a mask for the floor
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    
    # Apply morphological operations to clean up the mask
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # Find contours of the floor
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Find the largest contour (assume it's the floor)
        largest_contour = max(contours, key=cv2.contourArea)
        # Compute the center of the contour
        M = cv2.moments(largest_contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])  # X-coordinate of the center
            cy = int(M["m01"] / M["m00"])  # Y-coordinate of the center
            return (cx, cy)  # Return the position on the court
    return None