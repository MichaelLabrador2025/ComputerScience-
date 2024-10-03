# 2 basic functions
# functions have () at the end
# thins in () are parameters
#paramets are information needed 
print("hello world") # "hellow world" the parameters
input("what is your favorite animal:\n") 
#the \n is called an escape character (linebreak)

# Variables
# variables are a  way to store data for later use in the program
# syntax (grammar)
# <name> = <value>
x = 5    # x is the variable name, while 5 is the value
# snake naming convention - all lowercase under scores for spaces
# CONCISE: short and descriptive
username = "Osowski"                #define string  
fav_animal = "calugo"               #definie string 
total_poptarts = 12                 #define intinger
percent_complete = 23.52            #define float
first_leter = 'c'                   #define character   (character: single keyboard symbol)
is_cool = True                      #define boolean 

total_poptarts = 8                  #redefining variable

# Arithetic operator (basic math)
# + - * / ** % //
print(2+2)
print("2"+"2")
print("cat" + "dog")
print("cat" * 3)
print("cat" + 5)             #does not work

#working programs
x = input ("what is x?\n>")  #input function always returns strings 
x=int(x)
y = int(input ("what is y?\n>"))
print(int(x) + y)

#2. convert Celcius to Farenheight
temp_cel = 49
temp_far = (temp_cel *1.8) + 32
print (temp_cel + "° C is " + temp_far + "° F")

# conversion Functions
str()
int()
float()
bool()
bin()

#functions
#funtions are lot like varibales
#they have names
#they can be recalled for memory
#varbiable store a value, funtions store code
# def <name> ():

def potato():
    print("tomato")

potato()    #every funtion call needs parenthesis
            #even if no parameters


def jump(how_high):
    how_high = str(how_high) #convert int to string
    print("your jump " + how_high + " inches high.")

jump(14)

# Scope
# Global vs Local Variable
# Global: defined at no indentaion leve
# Local: defined at perameters and are local vars
# Global variables can be used anywhere
todd = "cool guy" #global variable becasue no indentation level

#local variables only exist in the context they where defined in 
def mu_function():
    smith = "not cool guy"
    print(todd)         
    print(smith)        #not cool guy
print (todd)            #cool guy
print (smith)

#return funcitons
#functions can also return values
# the value that is retuned is sent back to where the function was called
# similar to how variables work
def add_two_numbers(x,y):
  solution = x + y
  return solution 

answer = add_two_numbers(10,6)
print(answer)