import cv2
import requests
import os.path


class VideoProcessor:
    def __init__(self, images_path):
        self.images_path = images_path

    def capture_frames(self, output_path):
        # Initialize frame count
        frame_count = 0

        while True:
            # Generate the path for the current frame
            current_path = f'{self.images_path}/img_{frame_count}.jpg'
            # Check if the frame file exists
            if not os.path.isfile(current_path):
                print('No more frames to process')
                break

            # Read the frame from the file
            frame = cv2.imread(current_path)
            print(f'Processing frame {frame_count}')

            # Process the frame
            frame = self.process_frame(frame, frame_count)
            # Display the frame
            self.display_frame(frame, frame_count)
            # Save the frame to the output path
            self.save_frame(frame, frame_count, output_path)

            # Increment the frame count
            frame_count += 1

    def process_frame(self, frame, frame_count):
        # Load the Haar cascade for eye detection
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect eyes in the grayscale frame using the Haar cascade classifier
        eyes = eye_cascade.detectMultiScale(gray, 1.3, 4)

        # Get the width of the frame
        frame_width = frame.shape[1]

        # Process each detected eye
        for (x, y, w, h) in eyes:
            # Draw a rectangle around the eye
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Calculate the x-coordinate of the eye center
            eye_center_x = x + w // 2

            # Determine the side of the eye based on its position relative to the frame center
            if eye_center_x < frame_width // 2:
                eye_side = 'Left'
            else:
                eye_side = 'Right'

            # Display the side label near the eye
            cv2.putText(frame, eye_side, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        return frame

    def display_frame(self, frame, frame_count):
        # Display the frame in a window with the corresponding frame count
        cv2.imshow(f'Frame {frame_count}', frame)

        # Wait for a key press to proceed to the next frame
        cv2.waitKey(0)

        # Close all windows after the key press
        cv2.destroyAllWindows()

    def save_frame(self, frame, frame_count, output_path):
        # Save the frame to the output path with the corresponding frame count
        cv2.imwrite(f'{output_path}/img_{frame_count}.jpg', frame)


# Set the paths for input images and output frames
images_path = 'artifacts'
output_path = 'output'

# Create an instance of the VideoProcessor
processor = VideoProcessor(images_path)

# Start capturing frames and processing them
processor.capture_frames(output_path)
