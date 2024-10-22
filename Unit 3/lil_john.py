
def start():
    print("You and your son lil john go on a father and son trip to your favrite island. During this time a massive wind storm unexpectidly appeared pusing you into the The Bermuda Triangle.")
    print("you need to survive while providing for your son. in the distance you see a man. somthing is off about him. He has holes in his skin and his flesh is rotting. HES A ZOMBIE")
    print("pick options to survive, try and save you and lil john")
    do = int(input("enter 1 to start\n>"))
    if do == 1:
        dayone()
    else:
        print("you woke up and desited to go on a trip")
        start()
    return()

def dayone():
    print("its 6am acording to your sons basic survival sun clock. Your watch is all wonky and the radio keeps playing fien." +
           "the sun is rising fast and you and your son is sitting outside the plane" +
          "you hear a russle in the woods")
    print("whats your next step")
    print("1. go to the beach and try to look for planes or other things that have dropped off the plane")
    print("2. go to the forest to collect sticks and other things to start a fire")
    print("3. go in the plane to try and grab supplsies")
    adventure = int(input(">"))   
    if adventure == 1:
        beach_begining()
    elif adventure == 2:
        forest_begining()

def beach_begining():
    print("you desided to go to the beach with lil john while he is playing with sea shells you look up at the sky"+ 
      " and realize that the whole island is surounded by thick clouds and thunderstorms. but the sun perfeclty hits the island. It has been an hour and in the distanace you see a cave with a large entrance" + 
      "it appears to be glowing lil john says he is hungry, but you really want to chech it out. in the distance you hear a strange noise in the forest.")
    input("1. do you go to the forest" + 
          "2. do you go back to the plane" + 
          "3. do you check out the cave")
def forest_begining ():
    print("you desided to check out the noise"+
          "its a dog!! you ponder why its sitting out here when there is no sign of civilization"+
          "he starts barking and you look up............. zombies start chasing you!!!!" + " you tell lil john to get in the plane which is abt 100 meters and the dog comes with you")
    input(1. )



start()