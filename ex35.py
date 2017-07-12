from sys import exit

def gold_room():
    print ("This room is full of gold. How much do you take?")

   # next = input("> ")
    next = int(input("> "))
    #if int in next:
       # how_much = int(next)
    #else:
        #dead("Man, learn to type a number.")

    if next < 50:
        print ("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    # lines 20 - 23 use the print function to print statement
    print ("There is a bear here.")
    print ("The bear has a bunch of honey.")
    print ("The fat bear is in front of another door.")
    print ("How are you going to move the bear?")
    # declared a variable and gave it the truth value of False
    bear_moved = False

# Makes an infinite loop
    while True:
        # asks for your input
        next = input("> ")
        # if user entered take honey, it prints "The bear looks at you... Good job!"
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        # if user enters taunt bear and bear has not moved, print statement
        elif next == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door. You can go through it now.")
            # bear_moved becomes true?
            bear_moved = True
        # if user enters taunt bear and bear has moved, print statement with "Good job!"
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")

        elif next == "open door" and bear_moved:   
            gold_room()
        else:
            print ("I got no idea what that means.")

def cthulhu_room():
    print ("Here you see the great evil Cthulhu.")
    print ("He, it, whatever stares at you and you go insane.")
    print ("Do you flee for your life or eat your head?")

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def haunted_room():
    print("A hole opens under you and you fall into a room.")
    print ("The room is foggy, among the mist you see a little girl crouched on the floor.")
    print ("Her head is down.")
    print ("What do you do?")

    next = input("> ")
    if "run" in next: 
        dead("She lifts her head and eats you")
    elif "attack" in next:
        print ("She body slams you unconcious and keeps you as a pet")
    elif "help" in next or "talk" in next:
        print ("She lifts her head suddently and you see a white light.")
        print ("You wake up alongside of the nearest highway")
    else:
        dead("She leaps on you and keeps you as her pet human.")
 

def dead(why):
    print (why, "Good job!")
    # clean exit
    exit(0)

def start():
    print ("You are in a dark room.")
    print ("There is a door to your right and left.")
    print ("Which one do you take?")

    next = input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    elif next == "neither":
        haunted_room()
    else:
        dead("You stumble around the room until you starve.")

# program begins with start function
start()