"""string functions """
#are a group of funtions that modify strings
#  .lower()
# .lower() changes the string to be all lower

# .upper() changes the string to uppercase
# . upper()

# .capitalize() capilizes the first letter
#("HELLO WORLD") --> "Hello world"

# . title() changes the entire string to title case (Caps first letter of world)
# "hello world" --> "Hello World"

# . Swapcase() inverts the capitalization of each character
# "Hello World" --> "hELLO wORLD"

x = "Lord of the Rings".lower()
x = x.lower()
print(x)


answer1 = int(input("give a whole number that is less than 5.\n>"))
answer2 = int(input("give a whole number that is equal to 5.\n>"))
answer3 = int(input("give a whole number that is greater than 5.\n>"))
answer4 = int(input("give a whole number that is not 5.\n>"))
answer5 = int(input("give a whole number that is less than or equal too 5.\n>"))

def tally_score():
    score = 0
    if answer1 < 5:
        score = score + 1
    if answer2 == 5:
        score = score + 1
    if answer3 > 5:
        score = score + 1
    if answer4 != 5:
        score = score + 1
    if answer5 <= 5:
        score = score + 1
    print("score = "+ str(score))
tally_score()




