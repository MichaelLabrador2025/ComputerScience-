# for loops rview
# forloops allow us to iterate through a list
# Iterate: to preform repeadedly 
# to look at every item in a list one by one. 


# Basic Syntax 

pokemon_cards = ["Squirtle", "Bidoof", "Zigzagoon", "Charizard"]

for card in pokemon_cards:
    print("the next card is..................")
    print(card)

route = ["Home", "Taco Bell", "The Park", "Goodwill", "Home"]
#if oyu need to look at mutiple list items during one iteration
#doing "For item in list" doesnt work 
#for iteam in list only allows you to access one list of item per literation
for locationm in route:
    print ("You are travelilng from " + locationm + " to " + locationm[1])
    #this doesnt work
#if you need to access multiple list items durkng the same iteration,
#using "For Variable in range()" is prefferred
for i in range(0,len(route)): #Creates a list [0,1,2,3,4,]
    try:
        print("You are traveling from" + route[1] + " to " + route[i+1])
    except:
        print("route finnished ")

