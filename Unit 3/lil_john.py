
def start():
    print("You and your son lil john go on a father and son trip to your favrite island.\n" +
           " During this time a massive wind storm unexpectidly appeared pusing you into the The Bermuda Triangle.\n"+ 
          " you emergancy land on the beach of a uknown island after barley making it out of the storm,\n"+
            "your planes wings are all srached up and damaged, but you can eaily replace them.")
    print("you need to survive while providing for your son. in the distance you see a man outs of the plane. somthing is off about him. He has holes in his skin and his flesh is rotting. HES A ZOMBIE")
    print("pick options to survive, try and save you and lil john")
    do = int(input("enter 1 to start\n>"))
    if do == 1:
        dayone()
    else:
        print("you woke up and decided to go on a trip")
        start()
    return()

def dayone():
    print("its 6am acording to your sons basic survival sun clock, you knew boyscouts would pay off, Your watch is broken. It keeps spinning in circles super fast and the radio keeps playing fien.\n" +
           "the sun is rising, you and your son sit in the fuslage wondering what to do next. the only problem is the poliot is no where to be found.\n " +
          "you hear a russle in the woods")
    print("whats your next step")
    print("1. go to the beach and try to look for planes or other things that have dropped off the plane")
    print("2. go to the forest to collect sticks and other things to start a fire")
    print("3. go in the back to try and grab supplsies")
    adventure = int(input(">"))   
    if adventure == 1:
        beach_begining()





def beach_begining():
    print("you desided to go to the beach with lil john while he is playing with sea shells you look up at the sky\n"+ 
      " and realize that the whole island is surounded by thick clouds and thunderstorms. but the sun perfeclty hits the island. It has been an hour and in the distanace you see a cave with a large entrance\n" + 
      "it appears to be glowing lil john says he is hungry, but you really want to chech it out. in the distance you hear a strange noise in the forest.\n")
    adventure2 = int(input("1. do you go to the forest\n" + 
                        "2. do you go back to the plane\n" + 
                        "3. do you check out the cave\n>"))
    if adventure2 == 1:
        beach_forest()
    if adventure2 == 2:
        beach_plane()

def beach_plane ():
    print ("you deside there is nothing to do at the beach\n you decide go to the plane and wait for the piolot who is no where to be found. \n lil john is behind you wondering where you are, you say your no sure and keep walking. \n " + 
           "as you go to the plane the clock shows 3pm.... how is that possible when it only feels like an hour gone by at most.\n you ask lil john which he has no Idea all of a sudden you and lil john look up and hear a terrifing scream\n" +
           "you peep and see the piolot getting ate by zombies. terrified you take lil john and book it")
    getout = int(input("1. do you go to the beach \n 2. do you go to the forest \n>"))
    if getout == 1:
        beach_plane_beach()




def beach_plane_beach ():
    print ("you decide to sprint to the beach you and lil john go to the cave to hide, while there you realize the zombies never leave the forest.\n in the cave you see etches in the stones. it shows a tribe interacting with people coming out of a spaceship\n"
           " it looks like the aliens are setting up a camp. on what looks to be a building letters are etched on the side of it.\n - Goverment Property Of The United States- \n then spiders strat coming out of the back of the canve. thousands of spiders come out \n"
           " so you and lil john run out leaving. once out the cave you see a fire in the distance")
    curiosity = int(input("1. do you go towards the fire\n 2.do you try to run back to the plane"))












    
def beach_forest ():
    print("you desided to check out the noise you thought you heard earlier you left lil john in the plane, as it could be the piolet......... or a zombie.\n" + 
          " you also need sticks to make a shelter because the plane is getting too hot to sit in.\n "+
          "while on the way you start to think what you saw was just a pitolet because zombies can be real. you look up and see a dog!! you ponder why its sitting out here when there is no sign of civilization\n"+
          "he starts barking and you look up............. zombies, they start chasing you!!!!" + " you tell lil john to stay in the plane which is abt 100 meters and the dog comes with you\n")
    forest_cave = int(input("1. do you run to the beach to destract the zombies from lil john\n"+
                        "2. do you go to the fuslage to stay with lil john\n>"))
    if forest_cave == 1:
        beach_forest_cave()
    
def beach_forest_cave ():
    print("you go sprint to the beach where you see the cave. the dog is in front of you already heading in that direction\n"+
          " you realize the zombies stoped following you and head into the cave. there is a eeire feeling and chill once you stepped in the cave.\n" + 
          " there are carvings of people worshiping some big building. it on the carving the building says goverment property. you realize it must be some sort of goverment secret\n ")
    scream = int(input("you hear a scream and have no time to think\n" + 
                       "1. Run back to the plane\n" +
                       "2. try and find the building\n>"))
    if scream == 1:
        beach_forest_cave_scream()

def beach_forest_cave_scream():
    print("you get back to the plane and see the piolot ontop of the plane.")
    save = int(input("1. you yell and distract the zombie \n" +
                     "2. you hide in the bushes and wait till the zombies leave\n>"))
    if save == 1:
        beach_gameover()
    elif save == 2:
        beach_forest_cave_scream_wait()
        

def beach_forest_cave_scream_wait():
    print("as you wait it out you see the piolet get mutilaited, lil john is still in the fulsage. he is about to walk out so you\n" +
          "what do you do?")
    sacrafice = int(input("1. yell to destract the zombies\n " +
                          "2. just stay quiet\n"))
    if sacrafice == 1:
        print("you yell and try to run away. you trip")
        beach_gameover()

    elif sacrafice == 2:
        each_forest_cave_scream_wait_quiet()



def each_forest_cave_scream_wait_quiet ():
    print ("while waiting you see lil john get out of the plane anyway, not wanting to see what comes next you look down, but just in time a jeep comes and takes the zombies out\n a person gets out and introudces himself as professor pie "
           "Dr.Pie - how did you guys get here? you explain that you crashed in the burmuda triangle and your plane crashed. Dr Pie says - no worry we'll get you out of here. \n he explains that the goverment has been doing many test on the weird beucase the time is diffrent making many things evolve faster\n "
           "he also explain how the tribe got zomnified becuase the bactiria and other illnesses you see a building that looks exacly like the one in the cave\n"
           "you ask Dr.Pie and he tells you not to worry about it. as you enter the building, there are no windows.\n you seem sceptical about whats in the building")



    



def beach_gameover():
    print ("you wake up from a terible nightmare you where getting chased by zombies, you go down to sit at the dinner table drinking coffee like normal.\n" +
           "you look at little john who look abit odd. as you peek out the window and see words: goverment property on the building you work at.\n" +
           "you remeber your nightmare and it all makes sence. you tell little john not to go to work but when you try and tell him he\n"+
           "lunges at you and bites you.... he is a zombie\n "
           "Game Over")
    start()
start()