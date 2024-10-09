wind = int(input("whats the wind MPH\n>"))


if wind >= 157:
    print("Category 5")
elif wind > 157:
    print("Category 4")
elif wind > 130:
    print("Category 3")
elif wind > 111:
    print("Category 2")
elif wind > 96:
    print("Category 1")
elif wind > 74:
    print("tropical storm")
else:
    print("just a windy day :0")