print """You enter a dark room with three doors. Do you go through door #1 or 
door #2 or door #3?"""

door = raw_input(">")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do"
    print "1. Take the cake."
    print "2. Scream at the bear"
    print "3. Walk out and close the door"

    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3":
        print "The bears wife is behind you and eats your head. Good job!"
    
    else:
        print "Well, that's no fun. You continue your boring life." 

elif door == "2":
    print "You see an empty hall that leads to a staircase and an elevator. Which do you take?"
    print "1. Take the staircase."
    print "2. Take the Elevator."
    print "3. Neither. You walk out and close the door."


    transportation = raw_input("> ")

    if transportation == "1":
        print "It's a never ending staircase, you die from exhaustion."
    elif transportation == "2":
        print "You get on the elevator but there are only two other floors. Which floor do you press?"
        print "1. The Basement"
        print "2. The roof"

        floor = raw_input("> ")
        if floor == "1":
            print "You see pewdiepie waiting for you in his lambo. You guy's live happily ever after."
        else: 
            print "You get to the roof only to be eaten by a piranha plant."
  
    else:
        print "The yiga clan captures you and offers you to Calamity Ganon in exchange for a lifetime supply of bananas. Good job!"

elif door == "3":
    print "The door opens into a 80's design themed living room. You see John wick on the couch petting his pet chihuahua. What do you do?"
    print "1. Kill his chihuahua"
    print "2. Steal his chihuahua"
    print "3. Sit on the couch"
    
    wick = raw_input("> ")
    if wick == "1":
        print "He kills you. Haha classic John Wick."
    if wick == "2":
        print "You escape to the roof of the building. Come to find John Wick is sitting on a yoga ball waiting for you. He shoots you in the head. Good job!"
    elif wick == "3":
        print "John offers you popcorn and takes you home later. Congrats."
else:
    print "You stumble around and fall on a knife and die. Good job!"

