from dcmotor import DCMotor
from time import sleep

motor = DCMotor(20, 21, pwmPin=16)

motor.forward(0.2)
sleep(1)
motor.backward(0.2)
sleep(1)
motor.stop()


