from gpiozero import Motor, PWMOutputDevice

class DCMotor(Motor):
    def __init__(self, forward, backward, pwmPin=None):
        super().__init__(forward=forward, backward=backward)
        if(pwmPin != None):
            self.speed = PWMOutputDevice(pwmPin)

    def forward(self, speed=None):
        if(speed != None):
            self.speed.value = speed
        super().forward()

    def backward(self, speed=None):
        if(speed != None):
            self.speed.value = speed
        super().backward()