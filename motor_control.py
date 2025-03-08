import RPi.GPIO as GPIO
import time

class MotorControl:
    def __init__(self):
        # Define motor GPIO pins
        self.LEFT_FORWARD = 17
        self.LEFT_BACKWARD = 18
        self.RIGHT_FORWARD = 22
        self.RIGHT_BACKWARD = 23

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(
            [self.LEFT_FORWARD, self.LEFT_BACKWARD, self.RIGHT_FORWARD, self.RIGHT_BACKWARD],
            GPIO.OUT
        )

        self.left_pwm = GPIO.PWM(self.LEFT_FORWARD, 100)
        self.right_pwm = GPIO.PWM(self.RIGHT_FORWARD, 100)
        self.left_pwm.start(0)
        self.right_pwm.start(0)

    def move_forward(self, speed=50):
        self.left_pwm.ChangeDutyCycle(speed)
        self.right_pwm.ChangeDutyCycle(speed)

    def stop(self):
        self.left_pwm.ChangeDutyCycle(0)
        self.right_pwm.ChangeDutyCycle(0)

    def adjust_direction(self, cx):
        mid_point = 320  # Assuming 640x480 frame
        if cx < mid_point - 50:
            self.turn_left()
        elif cx > mid_point + 50:
            self.turn_right()
        else:
            self.move_forward()

    def turn_left(self):
        GPIO.output(self.LEFT_FORWARD, GPIO.LOW)
        GPIO.output(self.RIGHT_FORWARD, GPIO.HIGH)

    def turn_right(self):
        GPIO.output(self.RIGHT_FORWARD, GPIO.LOW)
        GPIO.output(self.LEFT_FORWARD, GPIO.HIGH)

    def cleanup(self):
        self.stop()
        GPIO.cleanup()
