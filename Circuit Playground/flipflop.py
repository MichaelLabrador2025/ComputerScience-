from adafruit_circuitplayground import cp


import time


while True:
    if cp.switch:
        for i in range(0,5):
            cp.pixels[i] = ((25, 0, 0))  
        for i in range(5,10):
            cp.pixels[i] = ((0,0,0))
    else:
        for i in range(5,10):
            cp.pixels[i] = ((25,0,0))
        for i in range(0,5):
            cp.pixels[i] = ((0, 0, 0)) 