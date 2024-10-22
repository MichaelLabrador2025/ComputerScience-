
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
    print("its 6am acording to your sons basic survival sun clock. Your watch is all wonky and the radio keeps playing fien. the sun is rising fast and you and your son are sitting on the beach")
    print("whats your next step")
    print("1. go to the beach and try to look for planes or other things that have dropped off the plane")
    print("2. go to the forest to collect sticks and other things to start a fire")
    print("3. go in the plane to try and grab supplsies")
    adventure = int(input(">"))   
    if adventure == 1:
        
start()