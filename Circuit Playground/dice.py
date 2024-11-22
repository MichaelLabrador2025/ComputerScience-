from adafruit_circuitplayground import cp
import random
import time

while True:
    if cp.button_a:
        cp.pixels.fill((0,0,0))
        roll = random.randint(0,10)
        for i in range(roll):
            cp.pixels[i] = (0,0,10)
        time.sleep(0.25)
    if cp.button_b:
        cp.pixels.fill((0,0,0))