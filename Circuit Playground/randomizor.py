from adafruit_circuitplayground import cp

import random 
       
while True:
    shake_threshold = 15.0  # Example threshold value
    x, y, z = cp.acceleration
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        apple = random.randint(0,255)
        ORANGE = random.randint(0,255)
        pear = random.randint(0,255)  
        cp.pixels[0] = ((apple, apple, apple))  
        cp.pixels[1] = ((ORANGE, ORANGE, ORANGE)) 
        cp.pixels[2] = ((pear, pear, pear)) 
        cp.pixels[3] = ((apple, ORANGE, pear)) 
        cp.pixels[4] = ((ORANGE, apple, pear)) 
        cp.pixels[5] = ((pear, ORANGE, apple)) 
        cp.pixels[6] = ((pear, ORANGE, pear)) 
        cp.pixels[7] = ((pear, ORANGE, pear)) 
        cp.pixels[8] = ((ORANGE, ORANGE, pear)) 
        cp.pixels[9] = ((apple, ORANGE, pear)) 