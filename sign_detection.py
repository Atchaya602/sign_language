# Use a pipeline as a high-level helper
from transformers import pipeline
import cv2

# Load the image classification pipeline with the specified model
pipe = pipeline("image-classification", model="RavenOnur/Sign-Language")

# Open the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

print("Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Save the current frame to a temporary file
    temp_image_path = "temp_frame.jpg"
    cv2.imwrite(temp_image_path, frame)

    # Perform the classification
    results = pipe(temp_image_path)

    # Display the classification results on the frame
    y_offset = 50  # Initial vertical offset for text
    for result in results:
        label = result['label']
        score = result['score']
        # Display each label and score at a new vertical position
        cv2.putText(frame, f"{label}: {score:.2f}", (10, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        y_offset += 30  # Increment vertical offset for the next label

    # Show the frame
    cv2.imshow("Live Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()