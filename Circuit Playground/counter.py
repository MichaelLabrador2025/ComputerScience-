from adafruit_circuitplayground import cp
import random
import time

count = 0
while True:
   
    if cp.button_a:
        count += 1
        time.sleep(0.25)
        cp.pixels[count] = ((0,0,10))
    if count >= 9:
        count = 9
    if cp.button_b:
        count = count - 1
        time.sleep(0.25)
        cp.pixels[count +1] = ((0,0,0))