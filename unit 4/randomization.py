"""python has four types of collections
tuple
set
>list
>dictionary
today, were going to focus on listtstststtsts

a list is a way to store more than one value in single variable
the values in the list are called items
items can be access by their index (position in the list) indices """
#Index                               0              1               2              3                    4   
import random
best_elden_ring_weapons =["Blasphemous Blade", "Moonveil", "Rivers of Blood", "Iron Ball", "Bloodhound's Fang"]
best_years= [1776, 1985,1994, 1957, 2016]
print(len(best_elden_ring_weapons))  #tells you number of iteams
print(best_years[1+3])
print(best_elden_ring_weapons[0])      #first Iteam
print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])

#list iteams can be changed 

best_elden_ring_weapons [3] = "Spike Fist"
print(best_elden_ring_weapons)

# list functions!
# .pop()
#removes an item at a given index
best_elden_ring_weapons.pop(1) #removes moonveil from list

# .remove()
# Removes an item by value- removes the first instance of the value
best_elden_ring_weapons.remove("Blasphemous Blade") #If the value doesnt exist it errors

# .append()
# adds the value as a new iteam to the end of the list
best_elden_ring_weapons.append("Death's Poker")

numbers = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
print(numbers)
# .sort()
# Sorts the numbers from least to greates
numbers.sort()
print(numbers)
# max()
#prints largest number
print(max(numbers))
# min()
#printes smallest number
print(min(numbers))

#Strings are just list of characters 
print("Oswoski"[2])