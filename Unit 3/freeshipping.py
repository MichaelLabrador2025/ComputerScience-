def freeshipping (prime, cost, age, consent):
    if prime == True or cost >= 25 and age >= 18 or consent == True:
        print ("free shipping")
    else:
        print("your cost will be ")