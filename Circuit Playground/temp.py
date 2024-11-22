from adafruit_circuitplayground import cp


while True:
    tempc = cp.temperature
    temp = (tempc * 9 / 5) + 32

    if temp < 78:
        cp.pixels[0] = (0, 0, 1)
    if temp > 78:
        cp.pixels[1] = (0, 0, 1) 
    if temp > 79:
        cp.pixels[2] = (0, 0, 1)  
    if temp > 80:
        cp.pixels[3] = (1, 1, 0)  
    if temp > 81:
        cp.pixels[4] = (1, 1, 0) 
    if temp > 82:
        cp.pixels[5] = (1, 1, 0)
    if temp > 83:
        cp.pixels[6] = (1, 1, 0)
    if temp > 84:
        cp.pixels[7] = (1, 0, 0)
    if temp > 85:
        cp.pixels[8] = (1, 0, 0)
    if temp > 86:
        cp.pixels[9] = (1, 0, 0)