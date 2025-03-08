import time
from line_follower import LineFollowerRobot
from motor_control import MotorControl
from sensor_interface import SensorInterface

def main():
    robot = LineFollowerRobot()
    motor_control = MotorControl()
    sensors = SensorInterface()

    print("Starting the robot...")
    try:
        while True:
            frame = robot.get_frame()
            binary_image = robot.detect_line(frame)
            cx = robot.process_frame(binary_image)

            if cx is not None:
                motor_control.adjust_direction(cx)
            else:
                motor_control.stop()

            time.sleep(0.05)  # Small delay to prevent excessive processing

    except KeyboardInterrupt:
        print("Stopping the robot.")
        motor_control.stop()
        robot.release_resources()

if __name__ == "__main__":
    main()
