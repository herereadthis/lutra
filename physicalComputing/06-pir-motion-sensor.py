"""Use a passive infrared motion sensor (PIR) to detect movement."""

from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print("You moved")
    pir.wait_for_no_motion()
    print("You stopped")
