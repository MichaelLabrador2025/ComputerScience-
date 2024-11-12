#allow you to change how loops aperate
# they do things like quit the loop early, skip current loop, or do nothing all 
# break, continue, pass 

#break 
#break exits the loop prematurely, befor it was suposed to end
#happens imidienty when ran
#program continues where the loop ended

#example
bag_of_fruit = ["apple", "orange","bug", "Kiwi", 'watermelon,', 'mango']

for fruit in bag_of_fruit:
    if fruit == "bug":
        print ("you found a nasty bug")
        break # the break statement exits the loop immediate and continues one
    else:
        print("you ate a " + fruit)

print("all done")


#continue
#skips the current loop
#doesnt exit current loop
#moves on to the current itteration 

#example
orders = [15, 20, 25, 23,100, 10, 23]

# Discount applying program 
# only apply discount for orders above $20

for order in orders:
    if order < 20:
        continue
    print("$" + str(order)+ " Order discounted 5% to $ " + str(order * 0.95))