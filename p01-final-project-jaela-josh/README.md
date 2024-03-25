# CSC226 Final Project



️**Author(s)**: Jaela Smith & Josh Wakin

️**Google Doc Link**: https://docs.google.com/document/d/1v2YvJGG8FC2l8poqLx3XhJK7QCOa9bB4wHdpYnG3NzQ/edit
---

**References**: 
https://www.w3resource.com/python-exercises/tkinter/python-tkinter-basic-exercise-12.php
https://stackoverflow.com/questions/3482081/how-to-update-the-image-of-a-tkinter-label-widget
https://www.geeksforgeeks.org/how-to-get-the-tkinter-label-text/
https://www.tutorialspoint.com/python/tk_label.htm

---

## Milestone 1: Setup, Planning, Design

️**Title**: Appalachian Apocalypse 

**Purpose**: To create an adventure via post apocalyptic appalachia

**Sources**: Choose Your Own Adventure


️**CRC Card(s)**:
[img.png](img.png)

[alt text](image/crc.png "Image of CRC card as an example. Upload your CRC card(s) in place of this one")

**Branches**: 
 
1. Branch 1 name: Jaela's Branch
2. Branch 2 name: Josh's Branch

---

## Milestone 2: Code

No README action items. Keep your issue queue up to date, and focus on your code. 🙃

Your repository should have, at a minimum, two branches; one for each partner, each with their contributions. 

---

## Milestone 3: Virtual Check-In

 

️**Completion Percentage**: 70%

**Confidence**: We feel confident that the program can simulate a story and obstacles that can kill the player making them start over.
However the big problem we have ran into is trying to implement more complex situations such as the player needing a specific item in order to overcome an obstacle (like needing a weapon in order to get through a location with an enemy)


Keep your issue queue up to date, and continue to refine your code!

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions

The game is controlled by the 4 decision buttons on the left side of the screen. The game will describe a situation through text and you
must choose from the decisions on the left how to deal with the situation. Choose carefully though as some decisions could lead you to an 
early ending!

### Errors and Constraints

Text alignment for the Text log: We were unable to get the text to align to the left of the screen, even with adjustments, after
the first line of text the next line always gets centered.

Room class constraints: In the original plan for this project we want the player to able to have a back and forth interaction with enemies
simulating combat, as a result any enemy the player encounters just end up with the player getting killed.

Error 263 from play sound extension: the playsound extension was used to play the music when the program is started, but everytime the command
playsound is called it immediately throws off an error labeled Error 263. Unable to determine the cause. 

### Reflection


-We selected the 'Choose your own adventure' assignment because we felt it would be the easiest project to add classes and GUI elements to,
and let us have a lot of creative freedom with the setting of the story aspect for the project. In Josh's version of the project he used 
functions to act as locations and also stored the story text in each function. The plan was to apply this same structure but instead building
using classes to create locations instead of functions and create GUI window in order to communicate the players input to the rooms. We planned
to use 3 classes: player, room, enemy. The player would keep track of the player health and inventory, the room would hold the responses to the 
players decisions and what decisions they can make, and the enemy was supposed to be a object that wouldnt let the player pass through a certain
way until its defeated(By the player using a weapon in there inventory.).

-The final product reflects this design very well but is still missing the enemy class implementation. The rooms do hold the decisions the player can
make as well reactions to the player decisions. We weren't able to create an enemy class because we were unable to able to figure out how to
get it to communicate with the player and the room object. However we were able to simulate an enemy encounter due to the flexiblity of the room class.
This solution dosn't allow for the player to fight back however, so rooms with enemies just became dead ends that killed the player.

-The biggest thing we learned is that the more open ended code is designed, the more use it can have when applying it to the
final product. One limit of the rooms class is you are limited to 4 inputs from the player because of the GUI layout. But we
quickly figured out that we could give a location more decisions for the player to make by nesting rooms within rooms. Like in the
camp location of the game, when you talk to your friend it opens a new room identical to the camp room, but with different decisions.

-The most difficult part of the project was getting different elements of the program to communicate with each other. Specifically
making the GUI window communicate with the room objects. So we made when a button is calls a decision within the room object,(Button 1
calls the decision 1 method in the room) that the decision is one of 4 types. Ethier move rooms, damage the player, give the player an item,
 and checking if a player has an item and changing its self to move the player if they have the required item.

-Over all we should have spent more time on the the decision methods within the room class so that the player could have more 
interesting choices (and consequences), and an enemy class so that player would have some combat related encounters.

