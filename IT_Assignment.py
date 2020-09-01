##Imports time so that I can slow down the execution
import time
##Variables for later, can be changed.
has_gun = False
has_knife = False
has_spanner = False
is_ded = False
guard_ko = False
current_room = "prison"

##Introduce the Story to the player
print("Behind the Lines")
print("You've just woken up from another day in the brig of the enemy POW base,\nbut today is like no other, as you see that someone has left the cell doors unlocked.")
print("After exiting your cell,")
while is_ded != True:   
    if current_room == "prison":
      print("You see the base armoury to your left, the fuel plant to the right, and the base exit infront of you.")
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
         print("You are in the depths of enemy territory")
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
          if has_gun == False:
            if has_knife == False:
              print("You are within the armoury, and you see a gun and a knife.")
              choice = input("Which do you choose? ")
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
        print("You go through the door, and you realise that you have entered the breakroom. \nYou are discovered and shot.")
        time.sleep(1)
        print("You died.")
        is_ded = True
      elif action == "look":
        print("You are in the machine hall, and you hear the sound of workers from the hall.")
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
      ##3 choices, nothing can be done here
      print("You head to the nexus of the fuel plant,\nand see that you could head to the refinery, the port or the tank farm.")
      print("What would you like to do?")
      print("Actions Available: Refinery, Port, Tanks")
      action = input(">>> ").lower()
      if action == "refinery":
        print("You head towards the refinery.")
        current_room = "refinery"
      elif action == "port":
        print("You head towards the port.")
        current_room = "port"
      elif action == "tanks":
        print("You head towards the tank farm.")
        current_room = "tank_farm"
    if current_room == "port":
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
        print("You enter the engine room.")
        print("You see the bilge access to your right, and the engine management console to your left.")
        print("What would you like to do?")
        print("Actions Available: Right, Left, Look.")
        action = input(">>> ").lower()
        if action == "look":
            print("You are within the engine room of the tanker.")
        elif action == "left":
            print("You head over the the engine management console.")