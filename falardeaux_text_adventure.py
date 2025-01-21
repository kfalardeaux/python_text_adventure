##### TEXT ADVENTURE PROJECT #####

### imports / exports ###

#file


### Define the Class ### 

class Player:

#set info that will be used for game progression/saving/loading 
    def __init__(self):
        self.item_one = "0"
        self.item_two = "0"
        self.item_three = "0" 
    
### Create the Main Function ### 

def main():
    print("\nWelcome...\n")
    player = Player()
    new_or_load(player)
    print("\nYou find yourself alone in the foyer of the Haunted House.\n")
    end = False
    while(not end):
        pick_a_room()
        choice_room = input(" ")
        if(choice_room == "1"):
            print("\nYou chose to go to the Main Bedroom.\n")
            print("The room is small and sad, with little decoration.\n",
                  "The faint smell of dust and complacency fills the air.")
            bedroom_one(player)
        elif(choice_room == "2"):
            print("\nYou chose to go to the Attic.\n")
            print("The space is surprisingly large, with cobwebs covering most of the ceiling above.\n",
                  "A lone record player sits in the corner.\n")
            attic_room(player)
        elif(choice_room == "3"):
            print("\nYou chose to go to the Basement.\n")
            print("The languid dampness of the basement seeps into your bones,\n",
                  "and you are unsure of the vague scent of decompisition.\n")
            basement(player)
        elif(choice_room == "4"):
            print("\nYou chose to go to the Guest Bedroom.\n")
            print("The room is even smaller and sadder than the Main Bedroom.\n",
                  "A light, floral scent hangs in the air.\n")
            bedroom_two(player)
        elif(choice_room == "5"):
            print("\nYou chose to go to the Living Room.\n")
            print("The space is quite large compared to other rooms, but barely furnished.\n",
                  "A strange buzzing sound seems to filter down from the ceiling.\n")
            living_room(player)
        elif(choice_room == "6"):
            print("\nYou chose to go to the Kitchen.\n")
            print("The stuffiness of the air inside chokes up your lungs,\n",
                  "and there is a powerful combination of rot and chemicals.\n")
            kitchen(player)
        elif(choice_room == "7"):
            print("\nYou tried to open the Front Door.\n")
            end = front_door(player)
             
        elif(choice_room == "0"):
            save(player)
            end = True
        else:
            print("\nA strange power rejects your answer.\n")
    print("\nCome adventure again.\n")
    
### Create the save/load/check Functions ###

def save(player):
    with open("save_data.txt", "w") as save_data:
        save_data.write(str(player.item_one) + "\n")
        save_data.write(str(player.item_two) + "\n")
        save_data.write(str(player.item_three) + "\n")
        save_data.close()
        print("\nYour game was saved successfully.\n")

def load(player):
    with open("save_data.txt", "r") as load_data:
        player.item_one = load_data.readline()
        player.item_two = load_data.readline()
        player.item_two = player.item_two.rstrip('\n')
        player.item_three = load_data.readline()
        load_data.close()
        print("\nYour progress has been restored.\n")

###def check_progress(player):

def new_or_load(player):
    print("\nWould you like to start a new game, or load an old one?")
    print("Enter 'N' for new, or 'L' to load.\n")
    check_save = input(" ")
    if(check_save == "N"):
        print("\nStarting your adventure...\n")
        print("\nSome time has passed since you last visited the Haunted House,\n",
              "and you have not been able to get it off of your mind.\n",
              "You decide to return to it one night, and as you quietly enter...\n",
              "\nWHAM!!!\n The door slams shut behind you!\n",
              "You try to open it, but to no avail!\n")
        print("\nSuddenly, you hear a low growl, and turn to see,\n",
              "a Gargoyle statue standing next to the Front Door.\n",
              "\n'I see you have a sense of adventure,' the Gargoyle says.\n",
              "'I'll test you to see just how adventurous you are!'\n")
    elif(check_save == "L"):
        load(player)
    else:
        print("\nDo you not want to play?\n")

### Create the Room Functions ### 

def bedroom_one(player):
    end = False
    while(not end):
        br1_menu()
        choice_br1 = input(" ")
        if(choice_br1 == "1"):
            print("\nThe sheets are yellow, and a sharp smell emanates from behind the pillows.\n",
                  "Would you like to move the pillows?\n")
            pillow = input("Y or N? ")
            if(pillow == "Y"):
                print("\nYou moved the pillows, and discovered a rotten apple resting against the headboard.\n",
                      "Perhaps it is someone's forgotten snack?\n")
            elif(pillow == "N"):
                print("\nProbably for the best; the pillows look sticky.\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_br1 == "2"):
            print("\nThe window has a large crack along the left of the pane, and there are dead flies at the bottom.\n",
                  "Would you like to look out the window?\n")
            window = input("Y or N? ")
            if(window == "Y"):
                print("\nYou walked to the window and peered out, but all you can see is your reflection staring back.\n",
                      "Perhaps it's too dark out right now to see.\n")
            elif(window == "N"):
                print("\nProbably for the best; the window looks drafty.\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_br1 == "3"):
            print("\nYou walked to the nightstand to search it, and found a vase next to an old photo.\n",
                  "Would you like to pick up the vase?\n")
            vase = input("Y or N? ")
            if(vase == "Y"):
                if(player.item_one == "0"):
                    print("\nThe vase has a faint floral smell, but is otherwise unremarkable.\n")
                elif(player.item_one == "1"):
                    print("\nYou noticed the floral smell coming from the vase,\n",
                          "and decided to put the flowers inside it.\n")
                    player.item_one = "2"
                    print("\nThe vase suddenly shattered, and an eye popped out!\n",
                          "You got LEFT EYE.\n")
                elif(player.item_one == "2"):
                    print("\nYou find it strange that the vase has somehow become unbroken,\n",
                          "but remind yourself the vase probably has no further use.\n")
            elif(vase == "N"):
                print("\nAre you sure?  The vase might be important...\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_br1 == "0"):
            print("\nYou left the Main Bedroom.\n")
            end = True
        else:
            print("\nA strange power rejects your answer.\n")

def attic_room(player):
    end = False
    while(not end):
        att_menu()
        choice_att = input(" ")
        if(choice_att == "1"):
            print("\nYou decided to check the violin, and noticed its strings still look taut.\n",
                  "Would you like to pluck the strings?\n")
            violin = input("Y or N? ")
            if(violin == "Y"):
                print("\nYou plucked at the strings, but they instantly snapped.\n",
                 "The strings must not have been as taut as you thought.\n")
            elif(violin == "N"):
                print("\nProbably for the best; you wouldn't want to ruin such a nice instrument.\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_att == "2"):
            print("\nYou went up to the record player, and realized it still functions.\n",
                  "Would you like to play some music?\n")
            record = input("Y or N? ")
            if(record == "Y"):
                if(player.item_three == "0"):
                    print("\nYou do not have any music to play right now.\n")
                elif(player.item_three == "1"):
                    print("\nYou placed the vinyl in the record player, and a song begins.\n",
                          "~~ the ADVicE of geNeraTions brings Us togetheR as onE~~\n")
            elif(record == "N"):
                print("\nAre you sure?  The record player might be important...\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_att == "3"):
            print("\nYou walked over to the piano, but the cover is down over the keys.\n",
                  "Would you like to open the cover?\n")
            piano = input("Y or N? ")
            if(piano == "Y"):
                print("\nYou opened the cover, but there are no keys underneath.\n",
                      "This piano must not have been well loved.\n")
            elif(piano == "N"):
                print("\nProbably for the best; people can be picky about their pianos.\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_att == "0"):
            print("\nYou left the Attic.\n")
            end = True
        else:
            print("\nA strange power rejects your answer.\n")

def basement(player):
    end = False
    while(not end):
        bas_menu()
        choice_bas = input(" ")
        if(choice_bas == "1"):
            print("\nYou went to search the desk.  It has files spread out all over it.\n",
                "Would you like to read a file?\n")
            desk = input("Y or N? ")
            if(desk == "Y"):
                print("\nYou tried to read a file, but it is nothing but lists of numbers.\n",
                      "Maybe the person is an accountant?\n")
            elif(desk == "N"):
                print("\nProbably for the best; it's likely very private information!\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_bas == "2"):
            print("\nYou decided to search the cabinet, and were suddenly hit by an overwhelming smell.\n",
                  "Would you like to open the cabinet?\n")
            cabinet = input("Y or N? ")
            if(cabinet == "Y"):
                if(player.item_two == "0"):
                    print("\nYou tried to open the cabinet, but the hinges seem to be rusted shut.\n")
                elif(player.item_two == "1"):
                    print("\nYou used the chemical on the hinges, and the cabinet flung open!\n",
                          "You got RIGHT EYE.\n")
                    player.item_two = "2"
                elif(player.item_two == "2"):
                    print("\nYou open the cabinet again but nothing new is there,\n",
                          "even though you took the source of the smell.\n")
            elif(cabinet == "N"):
                print("\nAre you sure?  The cabinet might be important...\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_bas == "3"):
            print("\nYou checked the stack of boxes, and found that one has something inside.\n",
                  "Would you like to open the box?\n")
            boxes = input("Y or N? ")
            if(boxes == "Y"):
                print("\nYou opened the box, but there is nothing inside.\n",
                      "Maybe it was just your imagination?\n")
            elif(boxes == "N"):
                print("\nProbably for the best; things are in boxes for a reason.\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_bas == "0"):
            print("\nYou left the Basement.\n")
            end = True
        else:
            print("\nA strange power rejects your answer.\n")

def bedroom_two(player):
    end = False
    while(not end):
        br2_menu()
        choice_br2 = input(" ")
        if(choice_br2 == "1"):
            print("\nYou went over to the plant and noticed it has beautiful flowers.\n",
                  "Would you like to smell them?\n")
            flower = input("Y or N? ")
            if(flower == "Y"):
                if(player.item_one == "0"):
                    print("\nYou smell the flowers, and several fall out, stem and all!\n",
                          "You got FLOWERS.\n")
                    player.item_one = "1"
                elif(player.item_one == "1" or "2"):
                    print("\nYou notice that flowers have mysteriously regrown,\n",
                          "but remind yourself the plant probably has no further use.\n")
            elif(flower == "N"):
                print("\nAre you sure?  The flowers might be important...\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_br2 == "2"):
            print("\nYou walked over to the closet and grabbed the door knob, but it is quite stiff.\n",
                  "Would you like to force it open?")
            closet = input("Y or N? ")
            if(closet == "Y"):
                print("\nYou pry open the door, and find yellowed hangers on the rack inside.\n",
                      "Hangers probably aren't very useful without clothes.\n")
            elif(closet == "N"):
                print("\nProbably for the best; the door looks rather stuck, anyway.\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_br2 == "3"):
            print("\nYou went to look in the mirror, but it is covered in dust and cobwebs.\n",
                  "Would you like to wipe them away?\n")
            mirror = input("Y or N? ")
            if(mirror == "Y"):
                print("\nYou wipe away the grime, but find that your reflection in the mirror is missing.\n",
                      "Perhaps this mirror is broken?\n")
            elif(mirror == "N"):
                print("\nProbably for the best; you have nothing to clean your hands with after.\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_br2 == "0"):
            print("\nYou left the Guest Bedroom.\n")
            end = True
        else:
           print("\nA strange power rejects your answer.\n")

def living_room(player):
    end = False
    while(not end):
        liv_menu()
        choice_liv = input(" ")
        if(choice_liv == "1"):
            print("\nYou went to check the coat hanger, and there is a single worn, blue jacket hanging there.\n",
                  "Would you like to check its pockets?\n")
            hanger = input("Y or N? ")
            if(hanger == "Y"):
                print("\nYou checked the pockets, but found some unidentifiable change in an unknown currency.\n",
                      "Perhaps the house's owner is not from here.\n")
            elif(hanger == "N"):
                print("\nProbably for the best; you don't know where that jacket has been.\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_liv == "2"):
            print("\nYou walked over and looked at the TV.  It is currently playing on a static channel.\n",
                  "Would you like to change the channel?\n")
            telv = input("Y or N? ")
            if(telv == "Y"):
                print("\nYou changed the channel, and a faint voice called out through the static:\n",
                      "'... one ... wor... .f..rom ... many ... loo.. ..or the lette..r..s ...'\n")
            elif(telv == "N"):
                print("\nYou did not change the channel, and the static continues.\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_liv == "3"):
            print("\nYou went to the couch, and saw a small glimmer shining from underneath.\n",
                  "Would you like to peek under the couch?\n")
            couch = input("Y or N? ")
            if(couch == "Y"):
                if(player.item_three == "0"):
                    print("\nYou peeked under and found a shining vinyl record!\n",
                          "You got RECORD.\n")
                    player.item_three = "1"
                elif(player.item_three == "1"):
                    print("\nYou notice that another record has appeared,\n",
                          "but remind yourself the record you have seems more important.\n")
            elif(couch == "N"):
                print("\nAre you sure?  There might be something important under there...\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_liv == "0"):
            print("\nYou left the Living Room.\n")
            end = True
        else:
            print("\nA strange power rejects your answer.\n")

def kitchen(player):
    end = False
    while(not end):
        kit_menu()
        choice_kit = input(" ")
        if(choice_kit == "1"):
            print("\nYou decided to search under the sink, and found a long line of chemicals.\n",
                  "One of the chemicals has a 'corrosive' warning label.\n",
                  "Would you like to pick up the chemical?\n")
            sink = input("Y or N? ")
            if(sink == "Y"):
                if(player.item_two == "0"):
                    print("\nYou grabbed the chemical, and the label says WD-40!\n",
                          "You got CHEMICAL.\n")
                    player.item_two = "1"
                elif(player.item_two == "1" or "2"):
                    print("\nYou notice that a second bottle of WD-40 has appeared,\n",
                          "but you already have as much as you need.\n")
            elif(sink == "N"):
                print("\nAre you sure?  The chemical might be important...\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_kit == "2"):
            print("\nYou walked over to the oven and opened it, revealing a pan of raw chicken.\n",
                  "Would you like to turn on the oven?\n")
            oven = input("Y or N? ")
            if(oven == "Y"):
                print("\nYou tried to turn on the oven, but nothing happened.\n",
                      "The uncooked chicken's stench persists.\n")
            elif(oven == "N"):
                print("\nProbably for the best; it must not be cooking yet for a reason.\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_kit == "3"):
            print("\nYou opened up the fridge and found a bowl of fresh fruit.\n",
                  "Would you like to take a piece of fruit?\n")
            fridge = input("Y or N? ")
            if(fridge == "Y"):
                print("\nYou take a piece of fuit, but it crumbles to dust in your hand.\n",
                      "It must not have been as fresh as it seemed.\n")
            elif(fridge == "N"):
                print("\nProbably for the best; never eat food from a source you don't trust!\n")
            else:
                print("\nA strange power rejects your answer.\n")
        elif(choice_kit == "0"):
            print("\nYou left the Kitchen.\n")
            end = True
        else:
            print("\nA strange power rejects your answer.\n")

def front_door(player):
    if(player.item_one == "2" and player.item_two == "2"):
        print("\nYou insert both Eyes into the statue, and they begin to glow.\n",
              "The Gargoyle speaks, 'What is the password?'\n")
        correct = ["adventure", "ADVENTURE"]
        password = input(" ")
        if(password in correct):
            print("\n'You have given the correct password.  You are now free to go.'\n",
                  "'Just remember to keep your sense of adventure, always.'\n")
            print("\nCONGRATS!  You Won!\n")
            return True
        else:
            print("\n'The password is incorrect.  Come back when you know it.'\n")
            return False
    else:
        print("\nYou do not have the items needed yet.\n")
        return False
        

### Menu Displays ###

def pick_a_room():
    print("\nWhere would you like to go?\n")
    print("Enter '1' to go to the Main Bedroom.")
    print("Enter '2' to go to the Attic.")
    print("Enter '3' to go to the Basement.")
    print("Enter '4' to go to the Guest Bedroom.")
    print("Enter '5' to go to the Living Room.")
    print("Enter '6' to go to the Kitchen.")
    print("Enter '7' to try and open the Front Door.\n")
    print("Enter '0' to save and come back later.\n")
def br1_menu():
    print("\nWhat would you like to inspect?\n")
    print("Enter '1' to check the bed.")
    print("Enter '2' to look at the window.")
    print("Enter '3' to search the nightstand.\n")
    print("Enter '0' to leave the Main Bedroom.\n")
def att_menu():
    print("\nWhat would you like to inspect?\n")
    print("Enter '1' to look at the violin.")
    print("Enter '2' to check out the record player.")
    print("Enter '3' to look at the piano.\n")
    print("Enter '0' to leave the Attic.\n")
def bas_menu():
    print("\nWhat would you like to inspect?\n")
    print("Enter '1' to search the desk.")
    print("Enter '2' to search the cabinet.")
    print("Enter '3' to check the stack of boxes.\n")
    print("Enter '0' to leave the Basement.\n")
def br2_menu():
    print("\nWhat would you like to inspect?\n")
    print("Enter '1' to admire the plant.")
    print("Enter '2' to check the bedroom closet.")
    print("Enter '3' to look in the mirror.\n")
    print("Enter '0' to leave the Guest Bedroom.\n")
def liv_menu():
    print("\nWhat would you like to inspect?\n")
    print("Enter '1' to search the coat hanger.")
    print("Enter '2' to look at the TV.")
    print("Enter '3' to check the couch.\n")
    print("Enter '0' to leave the Living Room.\n")
def kit_menu():
    print("\nWhat would you like to inspect?\n")
    print("Enter '1' to search under the sink.")
    print("Enter '2' to open the oven.")
    print("Enter '3' to open the fridge.\n")
    print("Enter '0' to leave the Kitchen.\n")


### Start Program ###
main()
