# esle statement 
x = 10
if x > 0:       # not every if needs an else
    print("x is a positive Number")

# the second little buddy is the elif (elif)
elif x < 0:    
    print("x is a negative number")

else:           #else allways needs an if
    print("x is Zero")


light = input("what color is teh light?\n>")

if light.lower() == "green":
    print("go")

elif light.lower() == "yellow":
    print("STOP IF SAFE")

elif light.lower() == "red":
    print("stop")

else:
    print("YIELD")