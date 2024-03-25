######################################################################
# Author 1 : Mahak Kumawat
# Username: Mahak1729
# Author 2 : Josh Wakin
# Username: thealphagurlux
# Version : 1.x1
# Date / Time : 11 : 36 am

# Assignment: T01: Choose Your Own Adventure
# Purpose: To create a choose-your-own-adventure style game.

######################################################################
# Acknowledgements:

#   Original Authors: Dr. Scott Heggen and Prof. Brian Schack
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem

##### References for python

# https://stackoverflow.com/questions/70817998/why-does-this-while-loop-keep-looping-even-when-its-false-in-c

# https://stackoverflow.com/questions/21169097/how-to-change-the-scope-of-a-variable-in-a-function-python

# https://stackoverflow.com/questions/47661242/how-to-switch-true-to-false-in-python



######################################################################
from time import sleep

##############variables#############
##direction-         #created later but is used for input
delay = 1.2        # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False
HasSword = False
goblindead = False




#######################################################
#              ===Functions===                        #
#######################################################

#######Functions used for Chapter loops###########

def death():
    ##-END-##
    # The following is the end of the story. Don't change this section, unless you really want to.
    global HasSword
    global goblindead
    print("-----Y O U  H A V E  D I E D-----")
    print("-----Poor",username,"You've met a terrible fate!-----")

    print(">>>>>Press enter to try again<<<<<")
    HasSword = False
    goblindead = False
    input()
    room1()


#basic format for chapters to be copy and pasted##

def room():
    ######Intro
    print("desc")
    sleep(delay)
    print("To the North: ")
    sleep(delay)
    print("To the South: ")
    sleep(delay)
    print("To the West: ")
    sleep(delay)
    print("To the East:")

    ############
    direction=input("Choose a direction or action[North/South/East/West]: ")
    ###CHECK FOR VALID INPUT###
    while direction != "north" and direction != "south" and direction != "east" and direction != "west":
        print("Now",username," That wasn't a valid option.")
        direction = input("Choose a direction or action[North/South/East/West]: ")

    ###Print string based on input###
    if direction=="north":
        print("You go north.")

    elif direction =="south":
        print("You go south.")

    elif direction=="east":
        print("You go east")

    elif direction=="west":
        print("You go west")

#######################################################
#========= Different Rooms========#

#ROOM 1
def room1():

    global HasSword
    global goblindead
    ######Intro
    print("You stand in your makeshift campsite, a pitiful fire smoulders, sending black smoke to the sky.")
    sleep(delay)
    print("To the North: The Mystic Wood lies, fabeled to hold a great treasure.")
    sleep(delay)
    print("To the South: The Mouth of a cave, you can hear noises creep from within.")
    sleep(delay)
    print("To the West: A long road that you came from.")
    sleep(delay)
    print("To the East: A vast meadow of yellow flowers.")
    sleep(delay)
    ############
    direction = input("Choose a direction or action[Search the camp/North/South/East/West]: ")
    ###CHECK FOR VALID INPUT###
    while direction != "north" and direction != "south" and direction != "east" and direction != "west" and direction != "search camp":
        print("Now", username, " That wasn't a valid option.")
        direction = input("Choose a direction or action[Search the camp/North/South/East/West]: ")

    ###Print string based on input###
    if direction == "north":

        if goblindead==False:
            print("You go north.")
            sleep(delay)
            print("The trees tower over you almost nearly blocking out the sun.")
            sleep(delay)
            print("Suddenly a large goblin bandit jumps from the bushes roaring")
            sleep(delay * 3)
            ##check if user has sword
            if HasSword == True:
                print("The goblin lunges at you, your swords clash.")
                sleep(delay)
                print("You best the goblin, stabbing him in the chest.")
                print("You step over the goblins corpse, procceding deeper into the forest.")
                goblindead = True
                sleep(delay*3)
                room2()

            elif HasSword == False:
                print("The goblin rushes you, pulling back his arm for a mighty swing.")
                print("His sword makes contact with your neck, chopping it clean off.")
                death()
        elif goblindead == True :
            print("You go north.")
            sleep(delay)
            print("The trees tower over you almost nearly blocking out the sun.")
            sleep(delay*2)
            room2()

    elif direction == "south":
        print("You go south.")
        sleep(delay)
        print("You approach the cave, and as you enter you here a loud growl.")
        print("A vicious bear appreaches from the darkness.")
        sleep(delay*3)
        if HasSword==True:
            print("You swing your sword, plunging it into the bear.")
            print("The bear screams in pain as it swats you like a fly, slinging against the cave wall.")
            print("Your head makes first contact with the wall, the blow kills you instantly")
            sleep(delay*4)
            death()
        elif HasSword == False:
            print("The bear roars and swats you like a fly, slinging against the cave wall.")
            print("Your head makes first contact with the wall, the blow kills you instantly")
            death()
    elif direction == "east":
        print("You go east")
        room3()


    elif direction == "west":
        print("You look at the road to the west, this is where you came from.")
        sleep(delay)
        print("There's no turning back now. You must find the treasure hidden in the forest")
        sleep(delay)
        room1()

    elif direction == "search camp":
        print("You look around the camp for anything of interest.")


        sleep(delay)
        if HasSword == True :
            print("You don't see anything of interest - there's nothing here.")
            sleep(delay*3)
            room1()
        elif HasSword == False:
            print("You find your sword laying on a rock near the fire.")
            print(">>sword obtained!<<")
            HasSword=True
            sleep(delay*3)
            room1()

    else:
        room1()


###ROOM 2###

def room2():

    global HasSword
    ######Intro
    print("You stand at fork in the path with a little orange fox.")
    sleep(delay)
    print("The fox looks up at you and says 'It's dangerous here, you should go east where it is safe.'")
    sleep(delay)
    print("To the North: A fox with a un-passable wall of trees behind him.")
    sleep(delay)
    print("To the South: A path that lead back through the woods to your camp.")
    sleep(delay)
    print("To the West: Not far from you or the fox is a old treasure chest. ")
    sleep(delay)
    print("To the East: Tall grass the covers the entire forest floor.")

    ############
    direction=input("Choose a direction or action[Talk to fox/South/East/West]: ")
    ###CHECK FOR VALID INPUT###
    while direction != "talk to fox" and direction != "south" and direction != "east" and direction != "west":
        print("Now",username," That wasn't a valid option.")
        direction = input("Choose a direction or action[Talk to fox/South/East/West]: ")

    ###Print string based on input###
    if direction == "west":
        print("You approach the chest and attempt to open it-")
        if HasSword == True :
            print("You swing the chest open to reveal teeth and a tongue coming from inside.")
            print("This is no chest, its a mimic, a monster!")
            sleep(delay*3)
            print('Without hesitation you swing your sword, slicing the monster in half.')
            print('The monsters body plops to the ground before poofing into smoke.')
            sleep(delay*3)
            print('The smoke clears to reveal a huge pile of gold and jewels. You have found the treasure of the Mystic Woods!')
            print("")
            print('=====CONGRATULATIONS! YOU HAVE BEAT MORTAL QUEST AND FOUND THE TREASURE!=====')
            print('>>>Press Enter to go back to camp & keep exploring again!<<<')
            input()
            room1()

        elif HasSword== False:
            print("You swing the chest open to reveal teeth and a tongue coming from inside.")
            print("This is no chest, its a mimic, a monster!")
            sleep(delay * 3)
            print('The monsters tongue wraps around you, yanking you into the box.')
            print('The Mimic chest slams shut the teeth piercing you all over and killing you.')
            print('Faintly you can make out the voice of the fox saying')
            print('Should have gone East like I said, poor guy')
            sleep(delay*3)
            death()

    elif direction == "south":
        print("You go south.")
        sleep(delay)
        room1()

    elif direction == "east":
        print("You go east")
        print("About your fourth step into the tall grass- ")
        sleep(delay*2)
        print("A loud clank snaps through the air, you look down to see your foot to find it caugh in a bear trap.")
        sleep(delay)
        print('You slowly bleed out, as everything fades to black, you faintly here the fox say-')
        print("'Whoops, shouldve checked to see if that was actually safe first'")
        sleep(delay*2)
        death()

    elif direction == "Talk to fox":
        print("Fox:'Hi there Im lenny, the magical talking fox.'")
        sleep(delay*3)
        room2()

    else:
        room2()

def room3():
    ######Intro
    print("You stand in a field with yellow flowers as far as the eye can see to the south and east.")
    sleep(delay)
    print("To the North: The mystical forest. ")
    sleep(delay)
    print("To the West: A black smoke trail drifts into the sky from your camp.")
    sleep(delay)
    print('A low whisper fills the air, seeming to come from all directions.')

    ############
    direction=input("Choose a direction or action[North/West/Pick Flowers/Smell Flowers]: ")
    ###CHECK FOR VALID INPUT###
    while direction != "north" and direction != "south" and direction != "pick flowers" and direction != "smell flowers":
        print("Now",username," That wasn't a valid option.")
        direction = input("Choose a direction or action[North/South/East/West]: ")

    ###Print string based on input###
    if direction=="north":
        print("You go north.")
        print('Walking through the tree line deeper into the forest.')
        sleep(delay)
        room2()

    elif direction =="pick flowers":
        print("You pick the closet flower.")
        print("As you pluck the flower, the whispers erupt into unbearable screams.")
        print('The scream become so loud that your ear drums bust and your brain turns to mush.')
        sleep(delay*3)
        death()


    elif direction=="smell flowers":
        print("You lean down to smell the flowers, as you get closer to the ground, you can make out what the whispers are saying:")
        print("'Don't trust the fox, he lies.'")
        sleep(delay)
        room3()

    elif direction=="west":
        print("You go west")
        sleep(delay)
        room1()

    else:
        room3()


#############################################################
###### Intro///Asks the user to input their name.###########
print("You lie asleep under the night sky, dreaming of the two paths before you..")
sleep(delay)
print("The path of despair and death..")
sleep(delay)
print("Or the path of glory and riches!")
sleep(delay)
print("Glory that will have the people sing your name for all of time!")
sleep(delay)
print("Oh yeah - your name.")
sleep(delay)
## Ask user's name
username = input("What is your name again?..:  ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print("Welcome,", username, ", to Mortal Quest.")
sleep(delay)
print("Before you lie two paths. One path leads to riches unfathomable.")
print("The other, certain death. Choose wisely.")
sleep(delay)
print("")

sleep(delay * 2)
print("You awake at your campsite, at the edge of the mystical woods.")
print("Woods that are said to hold a great secret treasure.")
sleep(delay*2)
print("The crisp morning air flows over your face.")
print("The time for adventure is now.")

print("\n")
sleep(delay*2)

#########################################################################################################

room1()




#########################################################################################################


#########################################################################################################

