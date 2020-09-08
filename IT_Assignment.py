##Imports time so that I can slow down the execution
import time
##Variables for later, can be changed.
has_gun = False
has_knife = False
has_spanner = False
is_ded = False
fubar = False

##Sets the starting room
current_room = "prison"


##Void out function, when the player reaches an area that I havent coded yet.
def voidout(action):
    print(f"You step {action} and fall into the void, and you see a neon sign.")
    time.sleep(0.5)
    print("The sign says, YOU HAVE REACHED THE END OF THE CODED GAME")
    time.sleep(0.5)
    print("You have no idea what this means, but it doesn't sound good.")
    time.sleep(0.5)
    print("You died")
##Introduce the Story to the player
print("Behind The Lines")
time.sleep(0.5)
print("You've just woken up from another day in the brig of the enemy POW base,\nbut today is like no other, as you see that someone has left the cell doors unlocked.")
print("After exiting your cell,")
while is_ded != True:   
    if current_room == "prison":
      print("You see the base armoury to your left, the fuel plant to the right, and the base exit in front of you.")
      print("What would you like to do?")
      print("Actions Available: Forward, Left, Right, Look")
      action = input(">>> ").lower()
      if action == "left":
         ##They head toward the armoury
         current_room = "armoury"
         print("You head towards the armoury.")
      elif action == "right":
         ##They head toward the fuel plant
         current_room = "fuel_plant"
      elif action == "forward":
         ##The head toward the exit of the base
         current_room = "base_exit"
      elif action == "look":
         print("You are in the depths of enemy territory.")
    if current_room == "armoury":
      ##Everyting that happens within the Armoury
      print("You enter the armoury, and see the door to the machine shop lying ajar, and a spot where you could plant charges.")
      print("What would you like to do?")
      print("Actions Available: Backward, Left, Look, Plant Charges")
      action = input(">>> ").lower()
      if action == "backward":
         current_room = "prison"
         print("You head back to the prison.")
      elif action == "left":
         current_room = "machine_shop"
         print("You head to the machine shop.")
      elif action == "look":
          ##Check if they have either of the items
          if has_gun == False:
            if has_knife == False:
              print("You are within the armoury, and you see a gun and a knife.")
              choice = input("Which do you choose? ")
              ##Give them an item
              if choice.lower() == "knife":
                has_knife = True
                print("You pick up the knife.")
              elif choice.lower() == "gun":
                has_gun = True
                print("You pick up the gun.")
            else: 
              print("You are within the armoury.")
          else: 
            print("You are within the armoury.")
            
      elif action == "plant charges":
          ##Kaboom
          print("You plant the charges, but someone has closed the armoury door.")
          time.sleep(1)
          print("You Died")
          is_ded = True
    if current_room == "machine_shop":
      print("You enter the machine shop. There is an adjoining door to your left, and a closet on the right.")
      print("What would you like to do?")
      print("Actions available: Left, Look, Right, Backward")
      action = input(">>> ").lower()
      if action == "left":
          ##player killed by their stupidity
        print("You go through the door, and you realise that you have entered the breakroom. \nYou are discovered and shot.")
        time.sleep(1)
        print("You died.")
        is_ded = True
      elif action == "look":
        print("You are in the machine hall, and you hear the sound of workers from the adjoining door.")
      elif action == "backward":
        print("You head back to the armoury.")
        current_room = "armoury"
      elif action == "right":
        ##Rick Rolled
        print("You head into the closet.")
        print("You see a radio, that is currenty playing \nNever Gonna Give You Up by\nRick ASCII.")
        print(""",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*(/((#####%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&%&&&%%&&&%%%%%%%%%%%###%%%%%%%%%%###((******************
,*,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*/((((#####%%%%%%%%%&&&&&&&&&&&&&&&&&%%%%%%&&&%%%%%%%%%###########%#%%%%%%###(/******************
,*,,,,,,,,,,,,,,,,,,,,,,,,,,..,,..,,.,,,,,,,,,,,,,,,,,,*/(((((##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%######(((((((/////////((###%%#%%%###(/******************
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**/((((((##%%%%######################(((((///////////*********/((###%######((/****************,
,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,.......,,,,,,,,,,,,,,,,,,*//(####################((((((((((((((///////////////*********///(##%######((****************,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**/(##%%%%%###(##########((((((((((((((/////(((///////*********///(((####(((((/**************,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.......,,,,,,,,,,,,,,,,,,*//(#%%%%%###(((##########(((((((((((((((((//((/////////*******///(((#####((((/*************,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.,,,,,,,,,,,,,*******//##%%%%#####((((#########((((((((((((((((((((///////////*****////((#####(((//*************,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,.,,.......,,,,,,,,,,,,,,*******/##%%%%#####((############(((((((((((((((///////////////*****////(((##((((/*****************,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,********/(##%######################(((((((((((((((/////////***///*//*////(((##(((//*****************,,
,,,,,,,,,,,,,,,,,,,,,,,,,.........,,,,,,,,,,,,,,********/(###%#####################(((((((((((((((((////////**/**/////////(###(///**************,***,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,***********/(#%######(((###%%%%%%%%######(((((((((((((((((((((((//////////*//(##((/**********,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,.....,,,..,,,,,,,,,,,******,,*****/(######((((#############%%%%######((#################((((/////**/(#(((/***********,,,,,,,,,*
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,**,****,,,,,,****(#####(((((######%%%%%%%%########((////(###########(((///////***/(((((/******,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,.......,.,,,,,,,,,,****,,,,,,,,,,*/(((####(((((####%%#%%%%%%##########((//**/((######%######((///****//((((/(/*****,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,...,...,,,,,,,,,,,,**,**,,,,,,,,,,/((((((((///((#######################((///////((##(((///////////*****/(//**/((*,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,........,.,,,,,,,,,,,,,,,,,,,,,,,,,*((((#((/**//(((#####################((////////////(/////////********////***((*,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,*(((###/////((#####################((////////////////////////********(((///(/*,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,......,,.,,,,,,,,,,,,,,.,,,,,,,,,,,,,*(####(///((((####################((//////*//////////////**/*********/((/***,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,..,.......,,,,,,,,,,,,...,,,,,,,,,,,,*/#####(//(((#####################((/////////((((/////////////******////***,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,..........,,,,,,,,...........,,,,,,,,,,/((###/(((((#####################((////////((##((////////////***********,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,..........,,,,,,,,...........,,,,,,,,,,,**((##(((((#######################((((((/////(##(((//////////**///***,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,..........,,,,,,,............,,,,,,,,,,****/(#(//((((###################((((///////////((#((////////**///***,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,.,,,,,.,,,,,,,.............,.,.,,,,,,,******,*/((((((###############((((((//////////////((//////**********,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,...,,,,,,,...............,,,,,,,********,*/((((((#################((((((////////////(///////*******,,*,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,..,,,,,,,,.................,,,,,,******,,,*(((((((########%%%%%%###%###%#%##((((((/((///////*******,*,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,..,....,,,,,,,,..,....,,.,,,..,,,,,,,******,,,,,*((((((#############%######%%%#(///////(/////////*,,,,**,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,...,,,,,,,.................,...,,,,,,,,,,,,,,*(((#############((((((((((((///////////////////*,,,,***,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,..,..............,...,,,,,,,,,,,,,,,,/(((((############(((((((((//////////////////***//****,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,.......,,,,,,,,......................,,,,,,,,,,,,,,,,,(((#####(#############((((//(///////////////****(#/***,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,.,,,,,,,,,,,,,,,,,,,,..................,,,,,,,,,,,,,,,,*/((#######((##((((((((((//((////////////////*/***##((/***,**,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,.....,,..,,,,,,,,,.................,..,,,,,,,,,,,,,,,,*(*/(########(((((((((((///////////////////////*/***#%####(/*****,***,,**,,,,,,,,,
,,,,,,,,,,,,,,,,.......,,,,,,,,.................,,,,,,,,,,,,,,,,,,*((*(((##############(((((((///////////////////////***#%%%%%%##(/***********,,,,,,,,
,,,,,,,,,,,,...........,,,,,,,............,,,,,,,,,,,,,,,,,,,,,*/(##//(#(####################(((((//////////////////****%%%%%%%%%%##((/***********,,,*
,,,,,,,,,,,,..........,,,,,,,,.................,,..,,,,,,,,,*/(#####/((##(########################((////////////////***/%%%%%%%%%%%%%%%%%##(//********
,,,,,,,,,,,...........,,,,,,,,.......,,.,,,,...,,,,,,**//(#########(/((%#(###############%%%%%%%%#((//////////////(/***(%%%%%%%%%%%%%%%%&%%%%%%####((/
,,,,,,,,,,,...........,,,,,,,........,....,.,..,*/((##############%//((%%(######################(((((///////////((*****#%%%%%%%%%%%%%%%&&&&&&&&&%%%%%%
,,,,,,,,,,.........,,,,,,,,,,,,,,...,,,,.,,*/((####%%%#%%%%%%%%###(#%%%####((((((((/*/#########((##(((((///////(/******%%%%%%%%%%%%%%&%&&&&&&&&&&&&&&&
,,,,,,,,,,,..........,,,,,,,..,,,.,,,///((####%%%%%%%%%&&&&&%%%%%%##%##%%%#%#####(((/(###############((((////((//*****(%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&
,,,,,,,,,,,,,..,,...,,,,,,,,,,,*//(((#####%%%%%%%&&&&&&&&&&&%%%%%%####(#####%%%%##(/%(################(((((##(//*****/%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&
,,,,,,,,,,,,,.,,.,,,,,,,,*///(((#####%%%%%%&&&&&&&&&&&&&&&&&%%%%%&%####%##((######((#(###############(######///******#%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&
,,,,,,,,,,,,,,,,,,,,**//(((######%%%%%&&&&&&&&&&&&&&&&&&&&&&&%%%&&%####%%###%#####/((((##################((//*******(%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&
,,,,,,,,,,,,,,,**//((((######%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&%&&&#####%%##%%####(/((/(#################(///********(%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&
,,,,,,,,,,,,/(((((#####%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&(####%%##%%####(/((/(##############((///**********/%%%%%%%%%&&&&&&&&&&&&&&&&&&&&&&&&""")
        print("If this doesn't look right, expand the code window so that it fits.")
        is_ded = True
    if current_room == "fuel_plant":
      ##2 choices, nothing can be done here
      print("You head to the nexus of the fuel plant,\nand see that you could head to the refinery or the port.")
      print("What would you like to do?")
      print("Actions Available: Refinery, Port, Backward")
      action = input(">>> ").lower()
      if action == "refinery":
        print("You head towards the refinery.")
        current_room = "refinery"
      elif action == "port":
        print("You head towards the port.")
        current_room = "port"
      elif action == "backward":
          print("You head back to the prison block.")
          current_room = "prison"
    if current_room == "port":
      ##simple bool answers, only two choices
      print("You enter the port, and see an oil tanker docked at the port.")
      print("Do you want to board it?\nYes/No")
      action = input(">>> ").lower()
      if action == "yes":
        print("You stealthily board the tanker")
        current_room = "tanker"
      elif action == "no":
        print("The tanker leaves without you, but there is an unattended patrol boat nearby.\nDo you board it?\nYes/No")
        action = input(">>> ").lower()
        if action == "yes":
            if has_knife == True:
                print("You climb aboard the boat, and use your knife to bypass the ignition allowing you to escape.")
                time.sleep(1)
                print("You Survived")
                is_ded = True
            else:
                ##Non-deadly punishment
                print("You climb aboard the boat, but realise that the keys are missing from the ignition.")
                time.sleep(1)
                print("The guard discovers you as he climbs back aboard, and takes you back to the prison.")
                time.sleep(1)
                current_room = "prison"
        elif action == "no":
            if has_gun == True:
              print("The guard discovers you, but you shoot him before he can alert any of the other guards to your location.")
              time.sleep(1)
              print("You head to the patrol boat, and take some time to hotwire it,\nbut you get it running and escape to the horizon.")
              time.sleep(1)
              print("You Survived")
              is_ded = True
            else:
                print("The guard discovers you, and shoots you before you can get away.")
                time.sleep(1)
                print("You Died")
                is_ded = True
    if current_room == "tanker":
        ##If it ain't broke, break it
       if fubar == False:
          print("You have boarded the tanker right as it left port, and see the bridge to your right, the stairwell to the engine room to your left, and the lifeboats in front of you.")
          print("What would you like to do?")
          print("Actions Available: Forward, Left, Right, Look")
          action = input(">>> ").lower()
          if action == "look":
              print("You are on a moving oil tanker.")
              if has_spanner == False:
                print("You see a spanner lying on the deck")
                print("Do you pick it up?\nYes/No")
                action = input(">>> ").lower
                if action == "yes":
                    print("You pick up the spanner")
                    has_spanner = True
                elif action == "no":
                    print("You leave the spanner on the deck.")
          elif action == "forward":
              print("You get into one of the lifeboats, and start to put it over the side.\nThe seas begin to swell slightly and the lifeboat falls off its mountings.\nIt falls into the water, with you in it.")
              time.sleep(1)
              print("You get the motor turning and head towards friendly shores.")
              time.sleep(1)
              print("You Survived")
              is_ded = True
          elif action == "left":
              print("You head down to the engine room.")
              current_room = "engine"
          elif action == "right":
              print("You head to the bridge.")
              current_room = "bridge"
       else:
          print("As you head back up to the top deck, you can see that a fire has broken out aboard the ship.")
          time.sleep(1)
          print("The allied navy comes over to assist, and you make your way over to one of their ships.")
          time.sleep(1)
          print("You Survived")
          is_ded = True
    if current_room == "bridge":
        print("You approach the bridge, and you can see people within.")
        print("What would you like to do?")
        print("Actions available: Forward, Backward, Look.")
        action = input(">>> ").lower()
        if action == "look":
            print("You are on the exterior bridge wing.")
        elif action == "backward":
            current_room = "tanker"
            print("You head back to the main deck of the tanker.")
        elif action == "forward":
            print("You enter the bridge.")
            if has_spanner == True:
                print("You knock out the radio operator using the spanner, and begin to send a message to your allies.")
                if has_gun == True:
                    print("As his shipmates come around the corner, you begin to incapcitate them with your pistol.")
                    time.sleep(1)
                    print("Your allies fly in with a chopper and extract you from the tanker.")
                    time.sleep(1)
                    print("You Survived")
                    is_ded = True
                else:
                    print("As his shipmates come around the corner, you are discovered.\nThe captain throws you over the side.")
                    time.sleep(1)
                    print("You Died")
                    is_ded = True
            else:
                print("The radio operator discovers you, and shoves you off of the bridge, and you fall into the water.")
                time.sleep(1)
                print("You Died")
    if current_room == "engine":
        print("You see the bilge access to your right, and the engine management console to your left.")
        print("What would you like to do?")
        print("Actions Available: Right, Left, Look, Backward.")
        action = input(">>> ").lower()
        if action == "look":
            print("You are within the engine room of the tanker.")
        elif action == "left":
            ##You broke it
            print("You head over to the engine management console.")
            print("You have no idea what these buttons do, but you hit them anyway.")
            print("You hear an alarm go off nearby, and decide that its high time to get out of the engine room.")
            time.sleep(1)
            fubar = True
            current_room = "tanker"
        elif action == "right":
            print("You head to the bilge access.")
            print("As you head to the hatch, one of the crewmembers see you, and as you peer into the bilge, he shoves you into it.")
            print("You have no way out, and slowly drown.")
            time.sleep(1)
            print("You Died")
            is_ded = True
        elif action == "backward":
            print("You head back up to the top deck.")
            current_room = "tanker"
    if current_room == "refinery":
        print("You see the control room to your right, and a Jeep in front of you.")
        print("What would you like to do?")
        print("Actions Available: Forward, Right, Look, Backward.")
        action = input(">>> ").lower()
        if action == "backward":
            print("You head back to the Nexus")
            current_room = "fuel_plant"
        elif action == "forward":
            print("You hop in the Jeep, and see that the ignition switch is still primed.")
            time.sleep(1)
            print("You flee towards the horizon, and towards a friendly base.")
            time.sleep(1)
            print("You Survived")
            is_ded = True
        elif action == "look":
            print("You are within a refinery unit.")
        elif action == "right":
            print("You head to the control room.")
            current_room = "control"
    if current_room == "control":
        print("You see a control panel to your left, and a metering panel to your right.")
        print("What would you like to do?")
        print("Actions Available: Left, Right, Look, Backward")
        action = input(">>>").lower()
        if action == "push":
            ##Easter Egg
            print("You start pushing random buttons and turning random dials on the metering panel\nand find that the refinery outside is beginning to light on fire.")
            time.sleep(1)
            print("You realise that that is bad, and start running to that Jeep you saw earlier.")
            time.sleep(1)
            print("You get away in a nick of time.")
            time.sleep(1)
            print("You Survived", end ="")
            time.sleep(1)
            print(" barely.")
            is_ded = True
        elif action == "look":
            print("You are in the control room for the refinery.")
            print("You see a placard that says to not to Push any buttons, and the word Push seems to be prominent.")
        elif action == "left":
            print("You head over to the control panel, and turn the burners in the stack up to high.")
            print("A worker comes into the control room, and when he sees you, he proceeds to whack you over the head with a nearby shovel.")
            print("You Died")
            is_ded = True
        elif action == "right":
            print("You head over to the metering panel, and cut the flow to the tower.")
            print("You see a worker approaching the control room.")
            if has_knife == True:
                print("As he approaches the room, you shove your knife between the door jamb and the handle.")
                time.sleep(1)
                print("The worker assumes that he must have locked the door, so he goes to get his keys.")
                time.sleep(1)
                print("As he leaves, you retrieve your knife and make your way to the Jeep.")
                time.sleep(1)
                print("You leave in the Jeep, and as you're leaving the tower explodes.")
                time.sleep(1)
                print("Press any key to continue...")
                time.sleep(2)
                print("JK")
                time.sleep(0.5)
                print("You Survived")
                is_ded = True
            else:
                print("The worker comes into the control room, and when he sees you, he proceeds to whack you over the head with a nearby shovel.")
                print("You Died")
                is_ded = True
        elif action == "backward":
            current_room = "refinery"
            print("You head back into the refinery.")
    if current_room == "base_exit":
        print("You see the gate ahead of you, the guard shack to your left, and a motorbike to your right.")
        print("What would you like to do?")
        print("Actions available: Forward, Left, Right, Backward")
        action = input(">>> ").lower()
        if action == "backward":
            print("You head back to the prison block.")
            current_room = "prison"
        elif action == "right":
            print("You head out to the motorbike, and you see that its engine is ripped to shreds.")
            print("The guy who was working on it comes back and sees you.")
            print("He knocks you over the head with a large spanner.")
            print("You died")
            is_ded = True
        elif action == "left":
            print("You head towards the guard shack.")
            current_room = "guards"
        elif action == "look":
            print("You are at the exit to the enemy base.")
        elif action == "forward":
            print("You head towards the gate.")
            current_room = "gate"
    if current_room == "gate":
        print("You see freedom ahead of you, and a guard to the side of you.")
        print("Actions available: Forward, Left, Look, Backward")
        action = input(">>> ").lower()
        if action == "forward":
            print("You head towards freedom, and you die in the desert on your way there.")
            print("You died")
            is_ded = True
        elif action == "left":
            voidout(action)
            is_ded = True
        elif action == "look":
            print("You are at the exit gate to the enemy base, on the cusp on freedom.")
        elif action == "backward":
            print("You head back to the area with the motorbike.")
            current_room = "base_exit"
    if current_room == "guards":
        ##I ran out of time
        print("You see... nothing, just a white room, with empty walls.")
        print("Action available: backward")
        action = input(">>> ").lower()
        if action == "backward":
            print("You leave for the exterior.")
            time.sleep(1)
            current_room = "base_exit"
        else:
            print("You should really just leave this accursed building.")