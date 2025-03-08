import RPi.GPIO as GPIO

class SensorInterface:
    def __init__(self):
        self.sensor_pins = [5, 6, 13, 19]  # Example GPIO pins
        GPIO.setmode(GPIO.BCM)
        for pin in self.sensor_pins:
            GPIO.setup(pin, GPIO.IN)

    def read_sensors(self):
        return [GPIO.input(pin) for pin in self.sensor_pins]
