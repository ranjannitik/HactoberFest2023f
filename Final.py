import cv2
import numpy as np

# Load your images
image1 = cv2.imread('C://Users//ranja//OneDrive//Desktop//COW EMOTION//Cow1.jpg', cv2.IMREAD_COLOR)
image2 = cv2.imread('C://Users//ranja//OneDrive//Desktop//COW EMOTION//Cow3.jpg', cv2.IMREAD_COLOR)

# Create a dictionary to associate variable names with images
image_dict = {
    'Happy_Cow': image1,
    'Sad_Cow': image2
}

# Function to detect and classify the image
def detect_and_classify(frame, image_dict):
    best_match = None
    best_match_name = None
    threshold = 0.7  # Adjust the threshold as needed
    
    for name, template in image_dict.items():
        # Match the template using cv2.matchTemplate
        result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        
        if max_val > threshold:
            best_match = max_loc
            best_match_name = name
    
    return best_match_name

# Open the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera (usually the built-in webcam)

if not cap.isOpened():
    raise ValueError("Could not open the camera.")

while True:
    ret, frame = cap.read()  # Capture a frame from the camera

    if not ret:
        print("Error: Could not capture a frame.")
        break

    # Detect and classify the image
    detected_image = detect_and_classify(frame, image_dict)

    # Add a blue square to the center of the image if an image is detected
    if detected_image:
        h, w, _ = frame.shape
        square_size = min(h, w) // 5  # Adjust the size of the square as needed
        center_x = w // 2
        center_y = h // 2
        cv2.rectangle(frame, (center_x - square_size // 2, center_y - square_size // 2),
                      (center_x + square_size // 2, center_y + square_size // 2),
                      (255, 0, 0), 2)  # Draw a blue rectangle
        
        # Print the detected image's variable name as output
        print(f"Detected image: {detected_image}")

    # Display the current camera frame
    cv2.imshow('Camera Frame', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
