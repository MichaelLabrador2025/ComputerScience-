# For Loops
# This is Big deal
# For Loops allow the programmer to Repeat, or what we call loop

# Write a program that prints the numbers 1 - 10 
# Each on a new line

#fav_foods = ["eggs bennies", "fried chickie", "mac n cheese"]

#for <var> in  <list>:

for i in range(90,101):
    print(i)

#for food in fav_foods:
   # print(food)
    #Runs all of the lines inside the for loop
    #when it reaches the bottom of the list, it runs agiain
    #and moves on to the next item in the list
    #It ends when there are no list items left """





#create a count down 10-1 
"""for i in range(10,0,-1):   #start,stop,step
    print(i)"""





#create a forloop that adds values in 
"""numbers = [1,2,3,4,5]
total = 0
for number in numbers:
    total += number
print(total)"""


#Square of each number

"""int = [3,2,5,4,1]
newlist = []

for i in int:
    newlist.append(i*i)

print(newlist)"""



#Character count

"""stringy = input("Please enter a string\n>")
numnouls = 0
for s in stringy:

    if s.lower() in ["a","e","i","o","u"]:
        numnouls = numnouls + 1
print(numnouls)"""

#print Multiplication Table

"""try:
    multi = int(input("gimme an int yo!\n>"))
except:
    print("womp,womp!!")

n = 0

for i in range(0,multi+1):
    print(str(multi) +  " x " + str(i) + " = ", str(multi*i))"""


#create a list of names

"""names = ["peter", "John", "Paul", "Luke"]
for name in names:
    print("Hello, " + name + "!")"""

