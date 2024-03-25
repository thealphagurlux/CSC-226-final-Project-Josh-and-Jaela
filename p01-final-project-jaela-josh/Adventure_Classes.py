######################################################################
# Author: Josh Wakin, Jaela Smith
# Username: thealphagurlux
#
# T12: Events and GUIs
#
# Purpose: To hold classes used by the Adventure_v2.py to make a player
# and create rooms that allow the player to make decisions
#######################################################################




import tkinter as tk
from PIL import Image, ImageTk


class room:

    def __init__(self,BGlocation='GUI_images/testbackground2.png',
                 BGlabelRef = None,
                 TextLable = None,
                 PlayerRef = None,
                 RoomText ='You are in a Room',
                 DeathText = 'This is a long line of text thats supposed to say something in the room killed you',
                 damage = 0,
                 DB1 = None,
                 DB2 = None,
                 DB3=None,
                 DB4=None,
                 DecisionText = ['Decision','Decision','Decision','Decision'],
                 NewDecisionText = ['Decision','Decision','Decision','Decision'],
                 ResponseText = ['response','response','response','response'],
                 key1 = 'key' ,
                 key2 = 'key',
                 key3 = 'key',
                 key4 = 'key',
                 lockmessage = ['','','',''],
                 RoomItems = ['','','',''],
                 ChoiceType = [0,0,0,0],
                 ConnectingRoom1 = None,
                 ConnectingRoom2 = None,
                 ConnectingRoom3 = None,
                 ConnectingRoom4 = None):

        self.BGpath = BGlocation
        self.imageLabel = BGlabelRef
        self.MaintextLabel = TextLable
        self.D1 = DB1
        self.D2 = DB2
        self.D3 = DB3
        self.D4 = DB4
        self.decisiontext = DecisionText
        self.NewDescisionTxt = NewDecisionText
        self.roomitems = RoomItems
        self.Ckey1 = key1
        self.Ckey2 = key2
        self.Ckey3 = key3
        self.Ckey4 = key4
        self.lockmessage = lockmessage
        self.itembooleans = [False, False, False, False] ###set to true to keep player from getting
        self.responsetext = ResponseText
        self.defaultRMtxt = RoomText
        self.Deathtxt = DeathText
        self.CR1 = ConnectingRoom1
        self.CR2 = ConnectingRoom2
        self.CR3 = ConnectingRoom3
        self.CR4 = ConnectingRoom4
        self.Dtype = ChoiceType
        self.player = PlayerRef
        self.damage = damage
    def openroom(self):

        #Change Background
        print('Open Room')

        self.MainBG = Image.open(self.BGpath)
        self.MainBG = ImageTk.PhotoImage(self.MainBG)

        self.imageLabel.config(image = self.MainBG)
        self.imageLabel.pack()
        self.imageLabel.place(x=380, y=10)

        #Change text log

        self.MaintextLabel.config(text = self.defaultRMtxt)

        #Change button text


        self.D1.config(text = self.decisiontext[0])
        self.D2.config(text = self.decisiontext[1])
        self.D3.config(text = self.decisiontext[2])
        self.D4.config(text = self.decisiontext[3])

    def decision_1(self):

        ##Makes a decision,
        ##Decision Type depends on Dtype's value
        ## 0 = opens a different room
        ## 1 = damage player
        ## 2 = display text(used mostly to relay information)
        ## 3 = give player an item
        ## 4 = If player has specific item, remove it from inventory and change decision to open a new room

        #####MOVE ROOMS ###
        if self.Dtype[0]== 0:


            self.CR1.openroom()

            return self.CR1

        ### DAMAGE PLAYER ###
        elif self.Dtype[0] == 1:
            #subtract health from player
            self.player.damage_player(dmg=self.damage)

            self.MaintextLabel.config(text= self. responsetext[0])

            if self.player.health <= 0:



                return self

            else:
                print('Damage player')
                print(self.player.health)
                return self
        ###Just Display Flavor text###
        elif self.Dtype[0] == 2:

            self.MaintextLabel.config(text=self.responsetext[0])

            return self



        ##Check giveplayer item one time
        elif self.Dtype[0] == 3:

            if self.itembooleans[0] == False:

                #add item to inventory list on player
                itemtogive = self.roomitems[0]

                self.player.inventory.append(itemtogive)

                self.itembooleans[0] = True
                ## Creat notification of item found with a window

                itemwindow = tk.Tk(className='You Found an item!')

                itemwindow.geometry('300x150+570+50')

                itemttxt = tk.Label(itemwindow, text = 'You found a : ' + self.roomitems[0] + self.responsetext[0], wraplength= 250)

                itemttxt.pack()




                itemwindow.mainloop()





                print(self.player.inventory)

                return self



            else:

                self.MaintextLabel.config(text= 'Theres nothing interesting here.')

                print(self.player.inventory)

                return self




        ####Unlock pathway if player has specific item, and change dtype to 0.
        elif self.Dtype[0] == 4:


            print(self.player.inventory)


            for i in self.player.inventory:

                if i == self.Ckey1:

                    self.player.inventory.remove(i)

                    self.Dtype[0] = 0

                    self.MaintextLabel.config( text = self.responsetext[0] + ' (New path unlocked)')

                    self.decisiontext[0] = self.NewDescisionTxt[0]

                    self.D1.config( text = self.NewDescisionTxt[0])

                    break

            else:#if player dosnt have item change main text to say they can go through here.
                self.MaintextLabel.config(text = self.lockmessage[0])

            print(self.player.inventory)
            return self






        ### empty descions(-1, or any number that doesnt have an elif) just return the room to current room
        ###
        else:
            print('Empty Decision')
            return self
        ###



    def decision_2(self):

        ##Makes a decision,
        ##Decision Type depends on Dtype's value
        ## 0 = opens a different room
        ## 1 = damage player
        ## 2 = display text(used mostly to relay information)
        ## 3 = give player an item
        ## 4 = If player has specific item, remove it from inventory and change decision to open a new room

        #####MOVE ROOMS
        if self.Dtype[1] == 0:

            self.CR2.openroom()

            return self.CR2

        ### DAMAGE PLAYER
        elif self.Dtype[1] == 1:
            # subtract health from player
            self.player.damage_player(dmg=self.damage)

            self.MaintextLabel.config(text=self.responsetext[1])

            if self.player.health <= 0:

                return self

            else:
                print('Damage player')
                print(self.player.health)
                return self
        ###Just Display Flavor text###
        elif self.Dtype[1] == 2:


            self.MaintextLabel.config(text=self.responsetext[1])

            return self


        ####Give player an item one time
        elif self.Dtype[1] == 3:

            if self.itembooleans[1] == False:

                #add item to inventory list on player
                itemtogive = self.roomitems[1]

                self.player.inventory.append(itemtogive)

                self.itembooleans[1] = True
                ## Creat notification of item found with a window

                itemwindow = tk.Tk(className='You Found an item!')

                itemwindow.geometry('300x150+570+50')

                itemttxt = tk.Label(itemwindow, text = 'You found a : ' + self.roomitems[1] + self.responsetext[1], wraplength= 250)

                itemttxt.pack()




                itemwindow.mainloop()





                print(self.player.inventory)

                return self



            else:

                self.MaintextLabel.config(text= 'Theres nothing interesting here.')

                print(self.player.inventory)

                return self




        ####Unlock pathway if player has specific item, and change dtype to 0.
        elif self.Dtype[1] == 4:


            print(self.player.inventory)


            for i in self.player.inventory:

                if i == self.Ckey2:

                    self.player.inventory.remove(i)

                    self.Dtype[1] = 0

                    self.MaintextLabel.config( text = self.responsetext[1] + ' (New path unlocked)')

                    self.decisiontext[1] = self.NewDescisionTxt[1]

                    self.D2.config( text = self.NewDescisionTxt[1])

                    break

            else:#if player dosnt have item change main text to say they can go through here.
                self.MaintextLabel.config(text = self.lockmessage[1])

            print(self.player.inventory)
            return self





        ### empty descions(-1, or any number that doesnt have an elif) just return the room to current room
        ###
        else:
            print('Empty Decision')
            return self

        ###


    def decision_3(self):

        ##Makes a decision,
        ##Decision Type depends on Dtype's value
        ## 0 = opens a different room
        ## 1 = damage player
        ## 2 = display text(used mostly to relay information)
        ## 3 = give player an item
        ## 4 = If player has specific item, remove it from inventory and change decision to open a new room

        #####MOVE ROOMS
        if self.Dtype[2] == 0:

            self.CR3.openroom()

            return self.CR3

        ### DAMAGE PLAYER
        elif self.Dtype[2] == 1:
            # subtract health from player
            self.player.damage_player(dmg=self.damage)

            self.MaintextLabel.config(text=self.responsetext[2])

            if self.player.health <= 0:

                return self

            else:
                print('Damage player')
                print(self.player.health)
                return self
        ###Just Display Flavor text###
        elif self.Dtype[2] == 2:


            self.MaintextLabel.config(text=self.responsetext[2])

            return self


        ###Give player item one time
        elif self.Dtype[2] == 3:

            if self.itembooleans[2] == False:

                #add item to inventory list on player
                itemtogive = self.roomitems[2]

                self.player.inventory.append(itemtogive)

                self.itembooleans[2] = True
                ## Creat notification of item found with a window

                itemwindow = tk.Tk(className='You Found an item!')

                itemwindow.geometry('300x150+570+50')

                itemttxt = tk.Label(itemwindow, text = 'You found a : ' + self.roomitems[2] + self.responsetext[2], wraplength= 250)

                itemttxt.pack()




                itemwindow.mainloop()





                print(self.player.inventory)

                return self



            else:

                self.MaintextLabel.config(text= 'Theres nothing interesting here.')

                print(self.player.inventory)

                return self




        ####Unlock pathway if player has specific item, and change dtype to 0.
        elif self.Dtype[2] == 4:


            print(self.player.inventory)


            for i in self.player.inventory:

                if i == self.Ckey3:

                    self.player.inventory.remove(i)

                    self.Dtype[2] = 0

                    self.MaintextLabel.config( text = self.responsetext[2] + ' (New path unlocked)')

                    self.decisiontext[2] = self.NewDescisionTxt[2]

                    self.D3.config( text = self.NewDescisionTxt[2])

                    break

            else:#if player dosnt have item change main text to say they can go through here.
                self.MaintextLabel.config(text = self.lockmessage[2])

            print(self.player.inventory)
            return self





        ### empty descions(-1, or any number that doesnt have an elif) just return the room to current room
        ###
        else:
            print('Empty Decision')
            return self

        ###


    def decision_4(self):

        ##Makes a decision,
        ##Decision Type depends on Dtype's value
        ## 0 = opens a different room
        ## 1 = damage player
        ## 2 = display text(used mostly to relay information)
        ## 3 = give player an item
        ## 4 = If player has specific item, remove it from inventory and change decision to open a new room

        #####MOVE ROOMS
        if self.Dtype[3] == 0:

            self.CR4.openroom()

            return self.CR4

        ### DAMAGE PLAYER
        elif self.Dtype[3] == 1:
            # subtract health from player
            self.player.damage_player(dmg=self.damage)

            self.MaintextLabel.config(text=self.responsetext[3])

            if self.player.health <= 0:

                return self

            else:
                print('Damage player')
                print(self.player.health)
                return self
        ###Just Display Flavor text###
        elif self.Dtype[3] == 2:


            self.MaintextLabel.config(text=self.responsetext[3])

            return self

        ###Give player item one time
        elif self.Dtype[3] == 3:

            if self.itembooleans[3] == False:

                # add item to inventory list on player
                itemtogive = self.roomitems[3]

                self.player.inventory.append(itemtogive)

                self.itembooleans[3] = True
                ## Creat notification of item found with a window

                itemwindow = tk.Tk(className='You Found an item!')

                itemwindow.geometry('300x150+570+50')

                itemttxt = tk.Label(itemwindow, text='You found a : ' + self.roomitems[3] + self.responsetext[3], wraplength=250)

                itemttxt.pack()

                itemwindow.mainloop()

                print(self.player.inventory)

                return self



            else:

                self.MaintextLabel.config(text='Theres nothing interesting here.')

                print(self.player.inventory)

                return self




        ####Unlock pathway if player has specific item, and change dtype to 0.
        elif self.Dtype[3] == 4:

            print(self.player.inventory)

            for i in self.player.inventory:

                if i == self.Ckey4:
                    self.player.inventory.remove(i)

                    self.Dtype[3] = 0

                    self.MaintextLabel.config(text=self.responsetext[3] + ' (New path unlocked)')

                    self.decisiontext[3] = self.NewDescisionTxt[3]

                    self.D4.config(text=self.NewDescisionTxt[3])

                    break

            else:  # if player dosnt have item change main text to say they can go through here.
                self.MaintextLabel.config(text=self.lockmessage[3])

            print(self.player.inventory)
            return self





        ### empty descions(-1, or any number that doesnt have an elif) just return the room to current room
        ###
        else:
            print('Empty Decision')
            return self

        ###



########################################


    def connect(self,Room1 = None, Room2 = None, Room3 = None, Room4 = None):

        #sets room refernces to other room objects so that they can be opened
        #must be used after all room objects are created.

        self.CR1 = Room1
        self.CR2 = Room2
        self.CR3 = Room3
        self.CR4 = Room4










class player:

    def __init__(self,
                 name='Mr. Bob',
                 Health = 100,
                 inventory = [],
                 stats=(5,5,5,5)
                 ):

        self.name = name
        self.health = Health
        self.inventory = inventory
        self.stats = stats

    def damage_player(self,dmg = 0):

        self.health = self.health -dmg

        return self.health





def main():

    print('open class')













if __name__ == "__main__":
    main()