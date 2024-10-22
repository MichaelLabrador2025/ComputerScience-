#Nested if statement 

prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >= 18:
        print("FREE SHIPPING APPLIED!")
    elif consent:
        print("FREE SHIPPING APPLIED!")
    else:
        print("NO FREE SHIP FOR U...")
elif cost >= 25:
    if age >= 18:
        print("FREE SHIPPING APPLIED!")
    elif consent:
        print("FREE SHIPPING APPLIED!")
    else:
        print("NO FREE SHIP FOR U...")

else:
    print("NO FREE SHIP FOR U...")




# Decide if we need an umbrella
#need one if raining adn going outside
    
raining = input("is it raining outside?\n>")


if raining.lower() == "yes":
    outside = input("do you plan on going outside\n>")
    if outside.lowet("yes"):
        print("bring an umbrella")
    else:
        print("no umbrella")
else:
    print("no umbrella")