#there are a couple tues of loops in python
#the for loop lets you iterate through a lish
#^^^good for a set number of times ^^^
#Whileloop - for a unsertain amount of times 
#examples: passwords - you could get it right the first time or a million, or anywhere in between 


real_password = "ninjalowtaper"
entered_password = ""
attempt = 0
while entered_password != real_password:
    #ask for pasword
    entered_password = input("Please enter password\n>")
    

    #Check if password is correct 
    if entered_password == real_password:
        print("Access Granted")
    else:
        print("Access Denited \n Try Again")
        attempt += 1
        print("attempt")
        print(attempt)
print("Welcom!")

# With while loops, you need to be cafeful for infinite loops


count = 0
while True:
    count = count + 1
    print(count)



#Real World Example
    
user_input = ""

while user_input != "exit":
    user_input = input("enter somthing")
    print("Type exit to quit")
    print("you tuped:"+ user_input)
print("all done")

