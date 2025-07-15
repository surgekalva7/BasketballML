import cv2
from detect_ground import detect_ground_position
from basketball_2d import visualize_live_positions

def get_live_position():
    global cap
    ret, frame = cap.read()
    if not ret:
        return None
    # Detect ground position in the current frame
    return detect_ground_position(frame)

def main():
    global cap
    # Open video capture (0 for default camera, or provide video file path)
    cap = cv2.VideoCapture("video2.mp4")  # Use 0 for webcam or replace with 'video.mp4'

    # Start live visualization
    visualize_live_positions(get_live_position)

    # Release the video capture when done
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()