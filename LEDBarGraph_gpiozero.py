from gpiozero import LEDBarGraph
from time import sleep

graph = LEDBarGraph(16, 20, 21, 25, 24, pwm=True)

graph.value = 1/10
sleep(1)
graph.value = 3/10
sleep(1)
graph.value = -3/10
sleep(1)
graph.value = 9/10
sleep(1)
graph.value = 95/100
sleep(1)
