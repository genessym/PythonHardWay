from sys import exit
print("\nAs you start to gain back consciousness, you start to feel someone shaking you.")
print ("""\ney.... Hey! Wake up!
Who are you?""")
name = input("> ")

print("""\nHmmm, interesting choice...
Do you know where you are?""")
location = input("> ")
if location == "yes":
    dead("\nReally? Well I guess you don't need my help then. Good luck!")
else: 
    print("\nWell allow me to introduce myself, the names Bob! And I am the host of this interesting place.")
    print("""While Im sure you are dying to know why you are here, you probably should know where you are first. Well {}, you are at Simulator Model X Corp.""".format(name))
    print("""\nToday, you were chosen as our lucky contestant to try out our latest stimulator device. While confusing at first, it is actually quite simple. You will enter the door before you and will have the option of selecting 1 of the four doors. Each door leads to a real life world simulator where you will be faced with choices that could lead to eternal happiness or your impending doom.""")
    print("And the best part is, its actually all real! Sounds fun, right!?")
    print("\n.......Well Come on! Walk right on in!")

print("\n") 
print("\n") 

def dead(why):
    print (why, "Good job!")
    
    exit(0)

def beginning():
    print("\nYou enter a white room, before you stands 4 doors.")
    print("Which one do you take?")
    print("1. Door One")
    print("2. Door Two")
    print("3. Door Three")
   
    
    door = input("\n> ")
    if "one" in door:
        horror_simulator()
    elif "two" in door:
        office_simulator()
    elif "three" in door:
        game_simulator()
    else:
        dead("Bob stabs you in the back.")

def horror_simulator():
    print ("You wake up in the basement of an abandoned hospital.")
    print ("You hear a weird noise coming from upstairs")
    print ("What do you do?")
    print("1. hide")
    print("2. run upstairs")
    print("3. take a bat and run upstairs")
    decide = input("> ")
    if next == "1":
        print ("You die from inhaling dust from the floor.")
    elif next == "2":
        horror_simulator2()
    elif next == "3":
        print ("A floating head trips you and you die from a conussion.")
    else:
        dead("You hear someone walking down the stairs. As you peer your head around the corner, you see Will Smith. He takes your hand and teleports you to Hawaii and live the rest of your days in peace.")

def horror_simulator2():
    print ("\nAs you reach the first floor, you hear a baby crying. It sounds like it's coming from the left.")
    print ("Which way do you go?")
    print("1. Left")
    print("2. Right")
    decide = input("> ")
    if decide == "1":
        print("There's a 5 ft baby sitting on a yoga ball. He gets up and carries you bridal style. You both walk out the hospital and walk into the sunset.")
    elif decide == "2":
        print("A 20 ft tall tarantula chips off your head and feeds your body to it's babies")
    else:
        dead("A 10 ft tall clown chokes you to death from behind.")

def office_simulator():
    print("Phone rings. You suddenly wake up in a office cubicle at your everyday average paper export company.")
    print("You get up to make some coffees")
    print("As you reach the copy room, you see fat Marge your cubicle neighbor and Dan the copy guy.")
    print("1. Marge")
    print("2. Dan")
    print("3. Mark")
    print("Who do you talk to?")
    decide = input("> ")
    if decide == "1":
        print("You greet Marge and she blushes. She starts to walk toward you and winks.")
        marge()
    elif decide == "2":
        print("You greet Dave and he greets back. He asks \"how's the weather?\"")
        dan()
    elif decide == "3":
        print("You greet Mark and he fires you. Never greet your boss")
    else:
        dead("You die of life long depression due to lack of social life.")

def marge():
    print ("What do you do?")
    print("1. Wink back")
    print("2. Look disgusted")
    decide = input("> ")
    if decide == "1":
        print("Fast forward a month later, you are engaged to Marge and your picking out wedding decor colors.")
    elif decide == "2":
        print("Marge throws coffee in your face and your suit gets a stain. Leading to you dying from life long depression of never getting that coffee stain out.")
    else:
        dead("She becomes your stalker and kills your in your sleep at the age of 35.")

def dan():
    print ("What do you say?")
    print("1. \"The weather is great\".")
    print("2. \"Fuck you Dan\".")
    decide = input("> ")
    if decide == "1":
        print("Suddenly out of now, the copier breaks.")
        print("Dan cracks a smile and say's \"No worries, I got this.")
    elif decide == "2":
        print("Suddenly out of now, the copier breaks.")
        print("Dan frowns and says \"good luck fixing that\".")
        print("Your lack of copier workmanship triggers a lifelong existential crisis leading to your cruel death.")
    else:
        dead("You weirded Dan out")

def game_simulator():
    print("You wake up in the middle of a battle against Lucas (from Super Smash Bros)")
    print("Along the side, you see two figures who will fight for you: ")
    print("1. Phoenix Wright")
    print("2. Cooking Mama")
    print("Who do you choose?")
    decide = input("> ")
    if decide == "1":
        print("\"OBJECTION\" phoenix shouts. You both get obliterated by pk thunder.")
    elif decide == "2":
        print("As cooking mama begins to whisk with her all might. You both get obliterated by pk freeze.")
    else:
        dead("You flee and surprisingly... you get away.")




beginning()


