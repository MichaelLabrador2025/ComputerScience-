# Dictionary is a tpe of collection like a list
#A list is a collection of items in a sequence 
#a dictionary is diffrent
# dictionaries store data in key-value pairs
#you can retrive data quickly by using a unique key 
# instead of retriving it by idex (position)

#Example
# list uses brackits [], dictionaires use braces {}

michael = {
    "name" : "Michael",    #each line is a key which come in pairs
    "age": 17,
    "City": "Albertville",
    "Pets": 1,
    "Height": 8.9
    }

#each key must be unique
# Retreving values form a dictinary 

print(michael["name"]) # prints the name 
print(michael["age"])

# this will error if you give a key that DNE 
# print(michael[country])    # this errors bc country DNE

# .get allows you to retrive a value without erroring 
# when the key DNE
print(michael.get ("height"))
print(michael.get ("country","country not found")) #second peramiter is what is put when not found

#you can add new values to an existing dictionary 
michael["contry"] = "USA"

michael["age"] = 32

michael.pop("Pets")

# iterate through a dictionary using a for loop
for key in michael:
    print (key)
