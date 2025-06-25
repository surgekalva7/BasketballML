# FILE: basketball_detection.py

import cv2
import numpy as np

def detect_basketball(frame, lower_color, upper_color):
    """
    Detects a single basketball in the frame based on its color range.
    """
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the basketball color
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    basketball_center = None
    basketball_radius = 0

    if contours:
        # Find the largest contour (assumes the basketball is the largest object of the given color)
        largest_contour = max(contours, key=cv2.contourArea)

        # Approximate the largest contour to a circle
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)

        # Filter out small objects
        if radius > 10:  # Adjust this threshold based on the basketball size in the frame
            basketball_center = (int(x), int(y))
            basketball_radius = int(radius)

    return basketball_center, basketball_radius

def draw_basketball(frame, basketball_center, basketball_radius, is_on_ground):
    """
    Draws the basketball on the frame. Changes color to red if it hits the ground.
    """
    if basketball_center is not None:
        # Set the color based on whether the basketball is on the ground
        color = (0, 0, 255) if is_on_ground else (0, 255, 0)  # Red if on ground, Green otherwise

        # Draw the basketball
        cv2.circle(frame, basketball_center, basketball_radius, color, 2)
        cv2.putText(frame, "Basketball", (basketball_center[0] - basketball_radius, basketball_center[1] - basketball_radius - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

def detect_ground_contact(basketball_center, frame_height):
    """
    Determines if the basketball is in contact with the ground.
    """
    if basketball_center is not None:
        # Check if the basketball's y-coordinate is near the bottom of the frame
        if basketball_center[1] >= frame_height - 10:  # Adjust threshold as needed
            return True
    return False

def main():
    # Open the camera feed (0 for default camera, or replace with video file path)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    print("Press 'q' to exit.")

    # Define the color range for detecting the basketball (HSV values)
    # Adjust these values based on the basketball's color
    lower_color = np.array([5, 100, 100])  # Example: Orange lower bound
    upper_color = np.array([15, 255, 255])  # Example: Orange upper bound

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame.")
            break

        # Get the frame dimensions
        frame_height, frame_width, _ = frame.shape

        # Detect the basketball
        basketball_center, basketball_radius = detect_basketball(frame, lower_color, upper_color)

        # Check if the basketball hits the ground
        is_on_ground = detect_ground_contact(basketball_center, frame_height)

        # Draw the basketball with the appropriate color
        draw_basketball(frame, basketball_center, basketball_radius, is_on_ground)

        # Display the processed frame
        cv2.imshow("Basketball Detection", frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()