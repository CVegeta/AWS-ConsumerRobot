#print("Hello I am, Cesar!");

from gpiozero import Servo
from time import sleep

# Define GPIO pins for servos
claw_pin = 17  # GPIO pin for the claw servo
wrist_pin = 18  # GPIO pin for the wrist servo

# Create servo objects
claw_servo = Servo(claw_pin)
wrist_servo = Servo(wrist_pin)

# Function to open the claw
def open_claw():
    claw_servo.value = 1  # Set servo to fully open position
    sleep(1)  # Adjust duration as needed

# Function to close the claw
def close_claw():
    claw_servo.value = -1  # Set servo to fully closed position
    sleep(1)  # Adjust duration as needed

# Function to rotate wrist clockwise
def rotate_clockwise():
    wrist_servo.value = 1  # Set servo to rotate clockwise
    sleep(1)  # Adjust duration as needed

# Function to rotate wrist counterclockwise
def rotate_counterclockwise():
    wrist_servo.value = -1  # Set servo to rotate counterclockwise
    sleep(1)  # Adjust duration as needed

# Function to stop wrist rotation
def stop_rotation():
    wrist_servo.value = 0  # Stop rotating
    sleep(1)  # Adjust duration as needed

# Example usage
def main():
    open_claw()
    rotate_clockwise()
    sleep(2)  # Rotate for 2 seconds
    stop_rotation()
    close_claw()

if __name__ == "__main__":
    main()
