import random
num = random.randint(0,100)
print(num)
number = ""

def runit ():
    while num != number:
          numguess = int(input("guess a number\n>")) 
    if numguess < num:
            print("the number is greater")
            runit()
    elif numguess > num:
            print("the number is lower")
            runit
    elif numguess == num: 
            print("you got it")


