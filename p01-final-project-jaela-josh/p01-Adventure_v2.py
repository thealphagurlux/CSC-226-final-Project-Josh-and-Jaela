######################################################################
# Author: Josh Wakin, Jaela Smith
# Username: thealphagurlux
#
#
#
# Purpose: To create a choose your own adventure style game through a GUI window
#
# The window will display text and images and buttons.
# The player will click on the buttons to make decisions throughout a story
# conveyed through text and images in the window
#######################################################################

import time

import tkinter as tk

from tkinter import ttk

from PIL import Image, ImageTk

from Adventure_Classes import room

from Adventure_Classes import player

from playsound import playsound


#######GLOBAL VARIABLES#########

Gwindow = None

GDeathScreen = None

GB1 = None
GB2 = None
GB3 = None
GB4 = None

GBGLabel = None
GTextLog = None
GPlayerLabel = None

GPlayer = None

CurrentLoc = None

####functions######

###DECISION HANDLERS: Hand communication betweeen GUI and Current room obj
def decision1_handler():

    #communicates info between Button1 and the decision 1 method in the room obj
    global Gwindow
    global GPlayer
    global CurrentLoc
    global GDeathScreen

    CurrentLoc = CurrentLoc.decision_1()

    ##Check if player is dead

    ##If player is dead
    if GPlayer.health <= 0 :

        ##destroy main window
        Gwindow.destroy()

        ##Create death screen and assign it to global variable

        GDeathScreen = create_DeathScreen()

        #add game over image
        BGDeath = Image.open('GUI_images/GameOver.png')  ##
        BGDeath = ImageTk.PhotoImage(BGDeath)

        DBGLabel = tk.Label(GDeathScreen, image = BGDeath)
        # DBGLabel.config(width=500, height=650)

        DBGLabel.place(x=30, y=0)

        GDeathScreen.mainloop()


def decision2_handler():
    # communicates info between Button1 and the decision 1 method in the room obj
    global Gwindow
    global GPlayer
    global CurrentLoc
    global GDeathScreen

    CurrentLoc = CurrentLoc.decision_2()

    ##Check if player is dead

    ##If player is dead
    if GPlayer.health <= 0:
        ##destroy main window
        Gwindow.destroy()

        ##Create death screen and assign it to global variable

        GDeathScreen = create_DeathScreen()

        # add game over image
        BGDeath = Image.open('GUI_images/GameOver.png')  ##
        BGDeath = ImageTk.PhotoImage(BGDeath)

        DBGLabel = tk.Label(GDeathScreen, image=BGDeath)
        # DBGLabel.config(width=500, height=650)

        DBGLabel.place(x=30, y=0)

        GDeathScreen.mainloop()

def decision3_handler():
    # communicates info between Button1 and the decision 1 method in the room obj
    global Gwindow
    global GPlayer
    global CurrentLoc
    global GDeathScreen

    ###Specifies which method to call
    CurrentLoc = CurrentLoc.decision_3()

    ##Check if player is dead

    ##If player is dead
    if GPlayer.health <= 0:
        ##destroy main window
        Gwindow.destroy()

        ##Create death screen and assign it to global variable

        GDeathScreen = create_DeathScreen()

        # add game over image
        BGDeath = Image.open('GUI_images/GameOver.png')  ##
        BGDeath = ImageTk.PhotoImage(BGDeath)

        DBGLabel = tk.Label(GDeathScreen, image=BGDeath)
        # DBGLabel.config(width=500, height=650)

        DBGLabel.place(x=30, y=0)

        GDeathScreen.mainloop()


def decision4_handler():
    # communicates info between Button1 and the decision 1 method in the room obj
    global Gwindow
    global GPlayer
    global CurrentLoc
    global GDeathScreen

    ###Specifies which method to call
    CurrentLoc = CurrentLoc.decision_4()

    ##Check if player is dead

    ##If player is dead
    if GPlayer.health <= 0:
        ##destroy main window
        Gwindow.destroy()

        ##Create death screen and assign it to global variable

        GDeathScreen = create_DeathScreen()

        # add game over image
        BGDeath = Image.open('GUI_images/GameOver.png')  ##
        BGDeath = ImageTk.PhotoImage(BGDeath)

        DBGLabel = tk.Label(GDeathScreen, image=BGDeath)


        DBGLabel.place(x=30, y=0)

        GDeathScreen.mainloop()


##########[End Of handlers]############
def create_main_window():

    ##global Variables to assign main window components

    global GB1
    global GB2
    global GB3
    global GB4
    global Gwindow
    global GTextLog
    global GBGLabel
    global GPlayerLabel
    global GDeathScreen
    global GPlayer




    ##create main window

    window = tk.Tk(className=' Appalachian Apocalypse ')

    # window.minsize(width=1000,height=850)

    window.geometry('1000x850+100+0')

    Gwindow = window


    #PlayerName label
    my_label = ttk.Label(window, text = GPlayer.name, font= 'ariel')
    my_label.place(x=30,y=60)






    ###CREATE IMAGES############################################



    ###CREATE BACKGROUND####


    BGimage_1 = Image.open('GUI_images/testbackground1.png')##Camp image
    BGimage_1 = ImageTk.PhotoImage(BGimage_1)



    ##set First BG##
    BGLabel = tk.Label( text='camp', image= BGimage_1)

    BGLabel.place(x=380,y=10)

    GBGLabel = BGLabel



    ###CREATE BUTTONS############################################

    ##each button has a decison handler function that communicates to the room the player is in
    ## and is assigned to a global variable for reference on the top level

    B1 = tk.Button(window, command= decision1_handler)
    B1.place(x=0,y=400,width=350,height=50)
    GB1 = B1

    B2 = tk.Button(window, command= decision2_handler)
    B2.place(x=0,y=450,width=350,height=50)
    GB2 = B2

    B3 = tk.Button(window, command= decision3_handler)
    B3.place(x=0,y=500,width=350,height=50)
    GB3 = B3

    B4 = tk.Button(window,command= decision4_handler)
    B4.place(x=0,y=550,width=350,height=50)
    GB4 = B4



    ###CREATE TEXT LOG###
    textLog = tk.Label(window,width=85,height=15,text='This is a Text log',bg='cyan',anchor = 'nw',wraplength = 600 )

    textLog.place(x=380,y=350)

    GTextLog = textLog



def create_DeathScreen():

    global CurrentLoc


    Dwindow = tk.Tk(className='You died! :(')



    Dwindow.geometry('600x600+400+0')


    DeathB1 = tk.Button(Dwindow,text = 'Try Again?', command=main)
    DeathB1.place(x=100, y=500, width=350, height=50)

    ##create death text description
    deathtext = tk.Label(Dwindow, text = CurrentLoc.Deathtxt, wraplength= 400)
    deathtext.place(x=100, y=350, width=400, height=100)





    return Dwindow


def playmusic():


    playsound('audio/Zombies_Comin_For_My_Soul.wav', block= False)


def main():


    global GB1
    global GB2
    global GB3
    global GB4
    global Gwindow
    global GTextLog
    global GBGLabel
    global GPlayerLabel
    global GPlayer
    global CurrentLoc
    global GDeathScreen

    ##play music




    ##if there is a death screen open destroy it
    if GDeathScreen != None:

        GDeathScreen.destroy()

    GPlayer = player() ###Creates player object, later changes this to call a function that allows the player to customize player and stats

    create_main_window() ##Creates main window





    #create player image

    playerimage = Image.open('GUI_images/player.png')
    playerimage = ImageTk.PhotoImage(playerimage)

    playerI_label = tk.Label(Gwindow, image = playerimage )

    playerI_label.place(x=15, y=100)








    ###CREAT ROOMS FROM CLASS#####

    #This first room created will label what the different class specifications are

    # room1 = room( BGlabelRef = GBGLabel,## reference the label we will be changing
    #               BGlocation='GUI_images/testbackground1.png', ##Set room background
    #               TextLable= GTextLog, RoomText='You are in Room1',##Text that appears onscreen when room is opened
    #               DeathText='Something in the Room Kills you',
    #               PlayerRef = GPlayer,## Give the room a reference to a player object
    #               DB1 = GB1, DB2 = GB2, DB3=GB3, DB4 = GB4,#assign buttons
    #               damage = 0, ##How much to damage player if decision hurts them
    #               DecisionText=['Go north','Go East','Go West','Go South'],##Text that appears on buttons
    #               ResponseText=['response', 'response', 'response', 'response'],
    #               ChoiceType = [0,0,0,0]) # Dictates what type of decision is made 0=move rooms




    #This room is used for testing purposes
    TestingRoom = room( BGlabelRef = GBGLabel,## reference the label we will be changing
                  BGlocation='GUI_images/testbackground2.png', ##Set room background
                  TextLable= GTextLog, RoomText='You are in a secret test room, with a box sitting on the floor',##Text that appears onscreen when room is opened
                  DeathText='Something in the Room Kills you',
                  PlayerRef = GPlayer,## Give the room a reference to a player object
                  DB1 = GB1, DB2 = GB2, DB3=GB3, DB4 = GB4,#assign buttons
                  damage = 0, ##How much to damage player if decision hurts them
                  DecisionText=['Open Locked door','Go East','Go West','Go South'],##Text that appears on buttons
                  ResponseText=[' You unlock the Door with the gun (gun removed)' , ' response', 'response', 'response'],
                  NewDecisionText=['Return to Camp'],
                  RoomItems=['','key','',''],
                  key1 = 'key',
                  key2= 'key',
                  lockmessage= ['The door is locked you need a key.'],
                  ChoiceType = [4,3,-1,-1]) # Dictates what type of decision is made 0=move rooms,1=damage player, 2= Display text, 3 = give player an item, 4 = use item in player inventory to unlock the door.


    Mainmenu = room( BGlabelRef = GBGLabel,## reference the label we will be changing
                  BGlocation='GUI_images/background_mm.png', ##Set room background
                  TextLable= GTextLog, RoomText='Welcome to Appalachian Apocalypse! Press Start to begin!',##Text that appears onscreen when room is opened
                  DeathText='Something in the Room Kills you',
                  PlayerRef = GPlayer,## Give the room a reference to a player object
                  DB1 = GB1, DB2 = GB2, DB3=GB3, DB4 = GB4,#assign buttons
                  damage = 0, ##How much to damage player if decision hurts them
                  DecisionText=['Start Game','How to play','Credits',''],##Text that appears on buttons
                  ResponseText=['response', 'Appalachian Apocalypse is a text based adventure game where your goal is to make sure you in your friend survive a zombie outbreak in appalachia. To interact with the story use the 4 buttons on the left. Becareful of what you choose to do! Otherwise you might end up ending the story early.', 'A game by Josh Wakin & Jaela Smith, Main Menu Theme: Zombies Coming For My Soul, by Anthony Mays', 'response'],
                  ChoiceType = [0,2,2,-1])

    introroom = room( BGlabelRef = GBGLabel,## reference the label we will be changing
                  BGlocation='GUI_images/background_mm.png', ##Set room background
                  TextLable= GTextLog,
                  RoomText='Two years ago a strange virus swept over the town of Middlesboro KY, turning any one infected with it into a lanky pale creature with a blood lust. You and your friend escape from the city into the near by national park, living in the woods since the out break. About 2 days ago your friend fell deathly ill, you fear if he dosnt get any medicine soon he might die or worse, turn into one of those things. Its up to you to find him some medicine.',##Text that appears onscreen when room is opened
                  DeathText='Something in the Room Kills you',
                  PlayerRef = GPlayer,## Give the room a reference to a player object
                  DB1 = GB1, DB2 = GB2, DB3=GB3, DB4 = GB4,#assign buttons
                  damage = 0, ##How much to damage player if decision hurts them
                  DecisionText=['Next','','',''],##Text that appears on buttons
                  ResponseText=['response', 'response', 'response', 'response'],
                  ChoiceType = [0,-1,-1,-1])



    friendroom = room( BGlabelRef = GBGLabel,## reference the label we will be changing
                  BGlocation='GUI_images/background_camp.png', ##Set room background
                  TextLable= GTextLog, RoomText='You approach your friend, he looks very sickly.',##Text that appears onscreen when room is opened
                  DeathText='Something in the Room Kills you',
                  PlayerRef = GPlayer,## Give the room a reference to a player object
                  DB1 = GB1, DB2 = GB2, DB3=GB3, DB4 = GB4,#assign buttons
                  damage = 0, ##How much to damage player if decision hurts them
                  key4 = 'medicine',
                  lockmessage=['','','','You do not have any medicine to give him! You are going to have to leave camp to find some.'],
                  DecisionText=['Ask how he is doing.','Tell him a joke','Go Back','Give medicine'],##Text that appears on buttons
                  ResponseText=['He looks up at you with bags under his eyes and says with wheezey breathe: You know..Hanging in there,(He coughs) if your going east you better get something out of the tent to protect yourself.' ,'He starts to laugh but then errupts into a coughing fit.', 'You tell ask him why the chicken crossed the road, your friend looks up at you and begs you not to tell that joke again, he has heard it 1000 times.', 'You give your friend the medicine, a wave of relief comes over you.'],
                  NewDecisionText=['','','','Sit down with your friend [Proceed to Ending]'],
                  ChoiceType = [2,2,0,4])


    camp = room(BGlabelRef=GBGLabel,  ## reference the label we will be changing
                 BGlocation='GUI_images/background_camp.png',
                 TextLable=GTextLog, RoomText='You are in your camp, your friend sits on a log wheezing and cough. To the east you see the top of the vistor center for the park you are camped at. ',  ##Text that appears onscreen when room is opened
                 DeathText='Something in the Room Kills you',
                 PlayerRef=GPlayer,
                 DB1=GB1, DB2=GB2, DB3=GB3, DB4=GB4,
                 damage=0,
                 RoomItems=['','','','Machete'],
                 DecisionText=['Go East', 'Approach your friend.', 'Look around Camp', 'Search tent'],  ##Text that appears on buttons
                 ResponseText=['response', '', 'You stand at your camp in the woods. What you call home', ', your handy (and iconic) tool. Use this to protect yourself.'],
                 ChoiceType=[0, 0, 2, 3])


    vistor_center = room( BGlabelRef = GBGLabel,
                  BGlocation='GUI_images/background_vc.png',
                  TextLable= GTextLog,
                  PlayerRef = GPlayer,
                  RoomText='You stand in front of the parks vistor center, it has been long since abandoned since the zombie outbreak happened.'
                           'To the west is the woods where your campsite hides, to the east the ruins of Middlesboro. To the south, a highway that leads into a tunnel that goes through the mountains.',
                  DeathText=' this is a long set of text that is supposed to say Something in the Room Kills you',
                  DB1 = GB1, DB2 = GB2, DB3=GB3, DB4 = GB4,
                  damage = 100,
                  DecisionText=['Go West','Go East','Look around','Go South'],
                  ResponseText=['repsonse', 'response', 'The area around you is quite, occasionally a creak can be heard from the Vistor Center.', 'response'],
                  ChoiceType = [0,0,2,0])

    tunnelroom = room( BGlabelRef = GBGLabel,## reference the label we will be changing
                  BGlocation='GUI_images/background_tunnel.png', ##Set room background
                  TextLable= GTextLog, RoomText='You stand before a tunnel that burrows through the mountains that border Tennessee and Kentucky. In the mouth of the tunnel you can see the pavement sinking into the ground being swallowed by a hole. To the north is the old Vistor Center.',##Text that appears onscreen when room is opened
                  DeathText='Something in the Room Kills you',
                  PlayerRef = GPlayer,## Give the room a reference to a player object
                  DB1 = GB1, DB2 = GB2, DB3=GB3, DB4 = GB4,#assign buttons
                  damage = 0, ##How much to damage player if decision hurts them
                  DecisionText=['Go into the tunnel','Go North','Look around',''],##Text that appears on buttons
                  ResponseText=['response', 'response', 'The gaping maw of the tunnel stands before you. A tunnel that was used as main point of access to Tennesse before the outbreak happened.', 'response'],
                  NewDecisionText=['Go back to camp','','',''],
                  ChoiceType = [0,0,2,-1])




    tunnelroom2 = room(BGlabelRef=GBGLabel,  ## reference the label we will be changing
                      BGlocation='GUI_images/background_tunnel_enemy.png',  ##Set room background
                      TextLable=GTextLog,
                      RoomText='As you approach the mouth of the cave a low growl echos from the hole in the ground. You freeze in place as a pale humaniod figure crawls from the darkness on all fours. It rises on to two legs towering a foot over you. ',
                      ##Text that appears onscreen when room is opened
                      DeathText='You lose to much blood and pass out on the ground. The creature grabs you by the foot, and you are dragged into hole in the ground dissapearing into the abyss.',
                      PlayerRef=GPlayer,  ## Give the room a reference to a player object
                      DB1=GB1, DB2=GB2, DB3=GB3, DB4=GB4,  # assign buttons
                      damage=50,  ##How much to damage player if decision hurts them
                      DecisionText=['Attack the creature', 'Run Away', 'Look around', ''],
                      ##Text that appears on buttons
                      ResponseText=['You reach for your weapon, but before you can draw it, the creature reacts dragging its claws accross your chest. You take heavy damage.', 'You turn around to run but as soon as. You feel the a sharp pain across your back, you flinch and fall to your knees in pain. ', 'You can see the chest of the creature rising and falling as its cold gaze is fixed on you.', 'response'],
                      ChoiceType=[1, 1, 2, -1])



    city1 = room( BGlabelRef = GBGLabel,## reference the label we will be changing
                  BGlocation ='GUI_images/background_town.png', ##Set room background
                  TextLable = GTextLog, RoomText='You find yourself on the main street of the town. Run down building of old shops run along both sides of the street to the North.',##Text that appears onscreen when room is opened
                  DeathText ='Something in the Room Kills you',
                  PlayerRef = GPlayer,## Give the room a reference to a player object
                  DB1 = GB1, DB2 = GB2, DB3=GB3, DB4 = GB4,#assign buttons
                  damage = 0, ##How much to damage player if decision hurts them
                  DecisionText=['Go North','Go West','Look Around',''],##Text that appears on buttons
                  ResponseText=['response', 'response', 'The crumbling ruins of middlesboro surround you.', 'response'],
                  ChoiceType = [0,0,2,-1])

    hospital = room(BGlabelRef=GBGLabel,  ## reference the label we will be changing
                 BGlocation='GUI_images/background_hospital.png',  ##Set room background
                 TextLable=GTextLog, RoomText='You stand in front of a run down hospital. There could be some medicine still laying around.',  ##Text that appears onscreen when room is opened
                 DeathText='Something in the Room Kills you',
                 PlayerRef=GPlayer,  ## Give the room a reference to a player object
                 DB1=GB1, DB2=GB2, DB3=GB3, DB4=GB4,  # assign buttons
                 damage=0,  ##How much to damage player if decision hurts them
                 RoomItems=['','','','Hospital Key'],
                 key1= 'Hospital Key',
                 lockmessage=['The front door is locked and theres no other way in.'],
                 DecisionText=['Enter hospital', 'Go South', 'Look around', 'Search dead body.'],  ##Text that appears on buttons
                 NewDecisionText=['Enter hospital [Opened]'],
                 ResponseText=['You search the hospital', 'response', 'In front of you is a hospital and a rotten corpse laying on the pavement, behind you is the mainstreet of Middlesboro.', ' a key that unlocks the front door of the hospital.'],
                 ChoiceType=[4, 0, 2, 3])


    insideHospital = room( BGlabelRef = GBGLabel,## reference the label we will be changing
                  BGlocation='GUI_images/background_insideh.png', ##Set room background
                  TextLable= GTextLog, RoomText='You are in the lobby of the hospital.',##Text that appears onscreen when room is opened
                  DeathText='Something in the Room Kills you',
                  PlayerRef = GPlayer,## Give the room a reference to a player object
                  DB1 = GB1, DB2 = GB2, DB3=GB3, DB4 = GB4,#assign buttons
                  damage = 0, ##How much to damage player if decision hurts them
                  RoomItems=['medicine'],
                  DecisionText=['Search for medicine','Go outside','',''],##Text that appears on buttons
                  ResponseText=[' this should cure your friend!', 'response', 'response', 'response'],
                  ChoiceType = [3,0,-1,-1])


    winroom = room( BGlabelRef = GBGLabel,## reference the label we will be changing
                  BGlocation='GUI_images/background_end.png', ##Set room background
                  TextLable= GTextLog, RoomText='As the day goes by your friend returns to good health. [END]',##Text that appears onscreen when room is opened
                  DeathText='Something in the Room Kills you',
                  PlayerRef = GPlayer,## Give the room a reference to a player object
                  DB1 = GB1, DB2 = GB2, DB3=GB3, DB4 = GB4,#assign buttons
                  damage = 0, ##How much to damage player if decision hurts them
                  DecisionText=['','','',''],##Text that appears on buttons
                  ResponseText=['response', 'response', 'response', 'response'],
                  ChoiceType = [-1,-1,-1,-1])





    ###CONNECT ROOMS###


    TestingRoom.connect(Room1 = camp)
    Mainmenu.connect( Room1 = introroom)
    introroom.connect(Room1 = camp)

    camp.connect(Room1 = vistor_center, Room2 = friendroom, Room3 = None, Room4 = TestingRoom)
    friendroom.connect(Room3 = camp, Room4= winroom)


    tunnelroom.connect(Room1=tunnelroom2, Room2=vistor_center, Room3=None, Room4=None)
    tunnelroom2.connect(Room3 = tunnelroom )

    vistor_center.connect(Room1=camp,Room2=city1,Room3=camp,Room4=tunnelroom)
    city1.connect(Room1=hospital, Room2=vistor_center, Room3=None, Room4=None)
    hospital.connect(Room1 = insideHospital, Room2= city1,Room3=city1)
    insideHospital.connect( Room2 = hospital)




    ### Start First Room#####
    CurrentLoc = Mainmenu




    CurrentLoc.openroom()




    Gwindow.mainloop()

playmusic()
main()

