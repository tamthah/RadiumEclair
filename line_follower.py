import cv2
import numpy as np
import logging

class LineFollowerRobot:
    def __init__(self):
        # Initialize camera and motor control here
        self.cap = cv2.VideoCapture(0)  # Use the appropriate camera index
        self.setup_logger()

    def setup_logger(self):
        """Set up the logger for the application."""
        self.logger = logging.getLogger('LineFollowerRobot')
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def detect_line(self, frame, color='black'):
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Apply a binary threshold to get a binary image
        _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
        return binary

    def follow_line(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            binary_image = self.detect_line(frame)
            # Find contours of the line
            contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            if contours:
                # Get the largest contour
                largest_contour = max(contours, key=cv2.contourArea)
                # Get the moments to find the center of the line
                M = cv2.moments(largest_contour)
                if M['m00'] != 0:
                    cx = int(M['m10'] / M['m00'])
                    # Control robot movement based on cx position
                    self.control_robot(cx)

            # Display the frame (for debugging)
            cv2.imshow('Line Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def control_robot(self, cx):
        # Implement motor control logic based on cx position
        # Example: if cx is left of center, turn left; if right, turn right
        self.logger.info(f'Center position: {cx}')
        # Add speed control logic here based on cx position
        # Add obstacle detection logic here

if __name__ == "__main__":
    robot = LineFollowerRobot()
    robot.follow_line()
