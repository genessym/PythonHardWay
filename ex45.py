

from sys import exit
from random import randint
import datetime_fun

class Scene(object):

    def enter(self):
        print ("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            if current_scene != None:
                next_scene_name = current_scene.enter()
                current_scene = self.scene_map.next_scene(next_scene_name)
            else:
                break 

        current_scene.enter()




class Entrance(Scene):

    def enter(self):
        print("*You start to gain back conciousness*")
        print("As you slowly open your eyes, you start to realize you are in the forbidden silent forest.")
        print("In front of you, you see a entrance to an underground tunnel.")
        print("As you peer in closer, engraved marks on the walls catch your attention.")
        print("\"Those who dare trespass, will face the fury of the great Yiga clan\".")
        print("You shrug your shoulders and walk toward the tunnel when suddenly")
        print("you hear a noise coming from the east.")
        print("What do you do?")
        print("1. Check out the noise ")
        print("2. Go back home")
        print("3. Enter the tunnel")
  
        answer = input('>')
        if answer == '1':
            print('You walk toward the noise and see something rustling in the bushes.')
            return 'silent_forest'
        elif answer == '2':
            print('You start to walk south of the entrance and follow the moonlight.')
            print('It is chilly out here, you look around for some firewood.')
            print('While looking, you find a lake.')
            print('As you start approach the lake to get a drink of water, you lose your balance')
            print('and fall in. Due to your lack of swimming expertise, you drown.')
            
            return 'death'
        else: 
            print('You walk down the staircase, entering the tunnel.')
            print('As you reach the ground, you find a wall torch to your right.')
            print('You pick up the wall torch and find that the tunnel splits into two directions.')
            print('You decide to go right because right is always right haha.')
            print('You walk to the end of the tunnel and find it is a dead end. As you turn around')
            print('to walk back, a sudden hole opens up under you and you fall onto a 15ft plate.')
            print('As you lift your head up, you see a 30 ft bokoblin in front of you with a bib on.')
            print('Bokoblin: Hohoho')
            print('The bokoblin picks you up and chomps your head off.')
            
            
            return 'death'

class SilentForest(Scene):
    
    def enter(self):
        date = datetime_fun.new_date
        print('You get closer')
        print('* POOF *')
        print('Grey smoke suddenly fills the air.')
        print('As the smoke begins to clear up, you see a small green round figure on the floor')
        print('Paku: Seesh.. I always get stuck in those bushes! Gosh..what time is it...,')
        print('Paku: Or better yet! What day is it today.. I need to find the hero!')
        print('You say: {}'.format(date))
        print('Paku: "AH! YOU SCARED ME! Who are you!?')
        print('...........')
        print('You wouldn\'t happen to be the next true hero!')
        print('...........')
        print("Paku: No response huh, then clearly you must be him! Wow, most heroes really aren\'t much talkers. Well that\'s fine.")
        print('All that is important is that you find the secret key to defeating the yiga clan and restore peace in Hyrule again.')
        print("And luckily for you! I will your oh so helpful guide!")
        print("Let\'s get going!")
        print('* Grey smoke suddenly appears again *')
        return 'transition'

class Transition(Scene):

    def enter(self):
        print('* Grey smoke begins to clear up *')
        print('You see that you\'re back in front of the tunnel entrace')
        print('Paku: Come on hero, what are you waiting for')
        print('* Paku runs in *')
        print('You decide to follow and walk down the stairs, entering the tunnel')
        print('As you reach the ground, you find a wall torch to your right.')
        print('You pick up the wall torch and find that the tunnel splits into two directions.')
        print('Paku: Well hero, which way?')
        print('1. left')
        print('2. right')

        answer = input('>')
        if answer == '1':
            return 'gorilla_room'
        else: 
            print('Paku: Guess right is always right, am I right?')
            print('You walk to the end of the tunnel and find it is a dead end. As you turn around to')
            print('to walk back, a sudden hole opens up under you and you fall onto a 15ft plate.')
            print('As you lift your head up, you see a 30 ft bokoblin in front of you with a bib on.')
            print('Bokoblin: Hohoho')
            print('The bokoblin picks you up and chomps your head off.')
            
            return 'death'

class GorillaRoom(Scene):

    def enter(self):
        print('You walk down the left tunnel and see a green light up ahead leading to a room opening.')
        print('You enter the room and find yourself in what looks like a jungle.')
        print('Paku: Well this is odd.')
        print('You hear a loud roar and decided to walk toward it')
        print('Pushing all the leaves out of your way, you eventually find yourself face to face with a gorilla sitting on a throne.')
        print('The throne completely surrounded by immense amounts of bananas')
        print('To the left and right of him, you see two yiga foot soilders fanning the gorilla in awe.')
        print('You step closer and the gorilla spots you.')
        print('What do you do?')
        answer = input('>')

        if 'talk' in answer:
            print('The gorilla turns his head in confusion.')
            print('Paku: I don\'t think he understands.')
            print('Yiga Footsoldier #1: "Well if you look who it is.')
            print('Yiga Footsoldier #2: The greaaaaat hero')
            print('You dare come to our hideout! You have some nerve!')
            print('But that\'s alright, it\'s more fun this way. I always wanted to see')
            print('the gorilla king in action.')
            print('* yiga footsoldier whispers to the gorilla king *')
            print('The gorilla angrily gets up and begins to run toward you. What do you do?')
            print('1. Run for your life')
            print('2. Shout "STOP"')
            print('3. Punch the gorilla')

            new_answer = input('>')

            if new_answer == '1':
                print('The gorilla king leaps into the air and falls onto you.')
                print('He rips off your leg and throws it.')
                print('You die from too much blood loss.')
                return 'death'
            elif new_answer == '2':
                print('The gorilla suddenly stops and looks at you.')
                print('Paku: ..... wow, he actually stopped! Do something to him before he gets mad again.')
                print('What do you do?')
                print('1. Tell a joke')
                print('2. Tell a really funny joke')
                print('3. Explain your situation in his language')

                decision = input('>')

                if decision == '1':
                    print('You end up telling the joke: ¿Sabes las dos palabras que te abrirán muchas puertas en el mundo?.... Tire y empuje.')
                    print('Silence fills the room')
                    print('The gorilla falls onto the ground and begins to laugh uncontrollably')
                    print('Gorilla: jajajajajajajajajaja')
                    print('His eyes begin to tear from so much laughter, it temporarily blinds him')
                    print('His footsoldiers run to his aid')
                    print('Yiga Footsoldier #1: God damn it! How did he know that spanish was the native language! ')
                    print('Yiga Footsoldier #2: Stop laughing so much Edwardo!')
                    print('Paku: This is our chance! Lets go!')
                    print('You see a small door behind the throne and run to it.')
                    print('You pass the doorway and a hole opens under you. You fall in')
                    return 'codeBreaker_room' 
            
                elif decision == '2':
                    print('You end up telling the joke: how many South Americans does it take to change a lightbulb?.... A brazillian.')
                    print('The footsoilders try to hold in their laughter')
                    print('You begin to feel a sense of relief until you look back at the gorilla who seems unamused')
                    print('The gorilla grabs yiga footsoldier #1 and throws him at you.')
                    print('You die from a concussion')
                    return 'death'
                
                else:
                    print('ooh ooh ooh eee eee eee aah aah aah.')
                    print('Silence fills the room')
                    print('Yiga Footsoldier #1: Woah man, why you gotta be so offensive')
                    print('Yiga Footsoldier #2: You know that is just an awful stereotype, right?')
                    print(' * The gorilla eyes start to tear up * ')
                    print('You try to apologize but the gorilla turns around and runs to the footsoldiers')
                    print('You look to Paku and he turns away')
                    print('Yiga Footsoldier #1: You monster! Any person who dares make Edwar.. I mean the gorilla king cry faces death!')
                    print('The footsoldier shoots an arrow through your heart')
                    return 'death'


            else: 
                print('The room is quiet.')
                print('Paku: *whispers* Did.... you really...just punch the gorilla.')
                print('The angered gorilla roars and hits his chest. He then leaps into the air,')
                print('and proceeds to do a 360 in mid air and dives straight down with his fist out.')
                print('You die from a direct K.O.')
                return 'death'
        else:
            print('Yiga Footsoldier #1: "Hey! Who are you!"')
            print('Yiga Footsoldier #2: "Intruder!"')
            print('* Yiga Footsoldier #1 shoots an arrow through your heart *')
            print('The footsoldiers laugh and you fall to the ground.')
            return 'death'


class CodeBreaker(Scene):

    def enter(self):
        
        print('You find yourself in the middle of a small white room,')
        print('only containing a keypad lock on the door')
        print('Paku: Wow, this looks so futuristic!')
        print('You walk toward the key pad and touch a random number')
        print('Suddenly you hear a voice coming from the key pad')
        print('Unknown voice: Haha, well what do we have here! A couple of intruders I see!')
        print('Unknown voice: Can\'t say I blame you though, this is our luxurious yiga clan hideout.')
        print('Unknown voice: Here we have the most advanced technology in all of hyrule!')
        print('Unknown voice: This room right here was created by our upmost intelligent leader, Master Kohga,')
        print('Unknown voice: It was designed to keep pesky intruders like yourself out from discovering our greatest secrets!')
        print('Unknown voice: Only the most intelligent class of people can figure out the three digit code to unlock this door')
        print('Karuk: That is including myself, Senior Karuk!')
        print('Simpletons like you could never, however it would be fun to see you try! Go ahead, I\'ll give three tries.')
        code = '{}{}{}'.format(0,1,2)
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses <= 3:
           print ("BZZZZEDDD!")
           guesses += 1
           if guesses == 2:
              print('Karuk: Hahaha, well what do we have! So much for the so called true hero!')
              print('Karuk: Can\'t even figure out something as easy as 0,1,2! Haha......')
           if guesses == 3:
               break
           print ("guesses =", guesses)
           guess = input("[keypad]> ")

        if guess == code:
            print ("The keypad clicks and the door swings open")
            print('Karuk: WHAT!?!? THIS CAN\'T BE, THE GREAT MASTER KOHGA DESIGNED THIS! YOU STAY RIGHT THERE!')
            print('Paku: Lets get the  out of here!')
            print('You run through the door and a hole opens under you. You fall in.')
            return 'master_room'
        else:
            
            print ("Karuk: Hahaha I told you! Only the best of the best can figure this out!") 
            print("Karuk: Now you will die the most impressive death!")
            print("The ceiling opens up and a unlimited supply of mighty bananas fall out. You drown.")
            return 'death'





class MasterRoom(Scene):

    def enter(self):
       print('Paku: ....ke...u....')
       print('Paku: ..wake... p....')
       print('Paku: wake up!')
       print('You open up your eyes.')
       print('You look around and see treasure chests, jewels and gold bars everywhere.')
       print('Paku: Woah... where are we..')
       print('You hear a noise coming from above you and look up and see a blademaster with his sword aimed at you.')
       print('You jump out the way dodging his attack.')
       print('The blade master lands on his feet.')
       print('Blade Master: I am quite impressed you dodged that, but make no mistake, that will not happen again!')
       print('Paku: Ah shit! He\'s gonna kill us... Quick, find a weapon!')
       print('You quickly scan the room and see three possible weapons, which do you go for?')
       print('1. Bug catching net to your left')
       print('2. torch behind you')
       print('3. Golden covered mop to your right')

       answer = input('>')
       
       if answer == '1':
           print('You grab the handle and proceed to charge at the blade master.')
           print('He dodges the attack and jumps back.')
           print('Blade Master: Hohoho You are quite skilled young one')
           print('He jumps up and ends up behind you. He tries to attack you with a upper attack')
           print('You go into block only to have your stick split into two. You proceed to be sliced in half')
           return 'death'

       elif answer == '2':
           print('You go to grab the torch and aim at the Blade Master.')
           print('Paku: You got this!')
           print('Sweat begins to fall down your forehead')
           print("As you are about to throw the torch at the blade masters head, your hand cramps up from the pressure.")
           print('You end up hitting yourself and dying from a concussion')

       else:
           print('You grab the handle and proceed to charge at the blade master.')
           print('He dodges the attack and jumps back.')
           print('Blade Master: Hohoho You are quite skilled young one')
           print('He jumps up and ends up behind you. He tries to attack you with a upper attack')
           print('You go in with a block and he jumps back.')
           print('Paku: WOW! Truly great swordmanship, you really are the true hero!')
           print('Blade Master: Looks like I\'m being too easy')
           print('Blade Master swings his sword and a gust of wind is formed.')
           print('You leap out of the way and slide toward the right side of the room.')
           print('You notice that he is standing under a golden chandelier. What do you do? ')
           print('1. Throw the golden covered mop at the chandelier')
           print('2. Throw Paku at the chandelier')
           print('3. Charge at the blade master with a overhead attack')

           new_answer = input('>')

           if new_answer == '1':
               print('You throw the map with all your strength')
               print('It gets stuck within the chandelier')
               print('The blade master goes for the opening and slices you in half')
               return 'death'

           if new_answer == '2':
               print('You fling Paku without hesitation toward the chandelier')
               print('Paku: NOOOOOOOO')
               print('Paku hits the chandelier and falls to the ground.')
               print('Due to Paku only being 5 pounds, nothing happens.')
               print('Paku is now unconscious and falls onto the blade masters shoulder.')
               print('Blade master chuckles.')
               print('In fear for his life, you charge to attack and aim for a over hand attack.')
               print('The blade master prepares with a block but you trick him and slide under him')
               print('Leaping up from behind him, you slice his legs.')
               print('The blade master falls to the ground and turns into a gust of red smoke,')
               print('leaving behind 3 ruby\'s and 4 mighty bananas.')
               print('You wake up Paku and carry him toward the exit.')
               return 'secret_room'

           else:
                print('The blade master grabs the bottom part of your mop and swings you around.')
                print('He swings you in a circle at 200 mph')
                print('You die from dizziness.')
                return 'death'
           

class SecretRoom(Scene):

    def enter(self):
        print('Paku opens his eyes suddenly and jumps')
        print('Paku: ATLEAST WARN ME NEXT TIME!')
        print('........')
        print('........')
        print('Paku: I guess you\'re sorry, I\'ll accept your apology just this once!')
        print('You smile and turn your head forward.')
        print('Walking down the narrow tunnel, you see a great opening up ahead draped in curtains.')
        print('You run toward it and pass through the curtains.')
        print('Paku: No way..... how...... can there be so many bananas')
        print('You found yourself in a bedroom made of mighty bananas.')
        print('Paku: Even the furniture is made out of bananas! ')
        print('\n')
        print('You look around, there is no door to be found.')
        print('Paku: There is no exit! Where is the secret room with the key to defeating Master Kohga.')
        print('Paku: There has to be something here if this is the last room!')
        print('Paku: Wait, what\'s that.')
        print('Paku points to the bed. You pull the sheets of and find a red banana')
        print('You: Um.. why is that banana red?')
        print('Paku: We don\'t have time for this, where is the secret weapon!?')
        print('................')
        print('................')
        print('Paku: You don\'t think that this.... it can\'t be..')
        print(' * alarms began to ring * ')
        print('Crap!')
        print('Paku: Wait, under the bed. It is a sword! Not just any sword but a Flame Blade')
        print('Paku: Yes! This must be it. We now must go to Hyrule Castle.')
        print('You grab the sword and look at Paku')
        print('Paku: Let\'s go!')
        print('Paku: ..... But I am pretty hungry * takes red banana *')
        print(' * grey smoke appears * ')
        return 'hyrule_castle'

class HyruleCastle(object):
    def enter(object):
        print('Paku: Ta - Dah! Welcome to hyrule castle')
        print('Paku points toward large door opening ')
        print('Paku: And that! That is the throne room, lets go  defeat Master Kohga once and for all')
        print('You run in and find Master Kohga lounging in a golden throne love seat in a bath robe')
        print('Kohga: who the heck are you?!')
        print('Paku: It\'s over Kohga! I bring to you the true hero of Hyrule. He has come here to defeat you!')
        print('Kohga: Ha! Defeat me! Don\'t make me chuckle! I am the greatest warrior ever known!')
        print('Kohga: I am the leader of the yiga clan!')
        print('Kohga: The strong!')
        print('Kohga: The Burly!')
        print('Kohga: The one!!')
        print('Kohga: The only!!!')
        print('Kohga: MASTER KOHGA')
        print('Kohga jumps in mid air and begins to float')
        print('Prepare yourself and watch a true leader!')
        print('He begins to summon massive stones and throws them at you.')
        print('You dodge each one!')
        print('Paku: HERO! You must take your weapon. Which do you take?')
        print('1. Red Banana')
        print('2. Flame Blade')
    

        answer = input('>')

        if answer == '1':
            print('Paku: What!? Why!')
            print('You take the red banana and shout to Kohga')
            print('Kohga: Ha! Are you begging for mercy?')
            print('You rise your right hand showing him the red banana')
            print('Kohga: Ha! I\'ve never been the merciless type since I am......')
            print('Kohga: Wait.... Is that what I think it is.')
            print('Kohga: Perfect smooth edges..')
            print('Kohga: Perfectly curved tail..')
            print('Kohga: Heavenly shining...')
            print('Kohga: Glorious red tint...')
            print('Kohga: That is the ...Red Dacca')
            print('Kohga: The only red banana to exist ever in Hyrule')
            print('\n')
            print('Kohga: GIVE IT TO ME')
            print('Master Kohga charges toward you from mid air')
            print('You slide to the right and Kohga falls to the ground')
            print('You sit on Master Kohga')
            print('Kohga: HOW DARE YOU SIT ON ME! OFF ME YOU INSOLENT RAT')
            print('Kohga proceeds to struggle, you take his arm and begin to twist')
            print('Kohga: OW OW OW! STOP IT STOP IT! ')
            print('Paku: Tap out!')
            print('Kohga: OKAY, OKAY! I TAP OUT, YOU WIN!')
            print('Paku: Wow..... that was easy')
            print('\n')
            print('How... How could I\'d be done in like this.... And by this guy, of all people! ')
            print('Heh no!')
            print('It\'s not over yet meheheheheh!')
            print('Time to bust out my serious moves! A secret technique taught by my father\'s mother\'s father! It will...destroy you!')
            print('Master Kohga slips out from under you, clasps his hand together and summons a 100 ft spiked ball to the ground')
            print('What do you do:')
            print('1. Do nothing')
            print('2. Take the flame blade and attack from the front')

            decision = input(">")
        
            if decision == '1':
                print('MWHAHAHA Only the leader of the yiga clan can use such a superior technique.')
                print('This technique developed by my father\'s mother\'s father has been taught from generation t....')
                print('* Ball begins to roll backward * ')
                print('Kohga: to gen... um wait... WAIT..')
                print('Ball squishes Master kohga')

                print('Paku: YOU DID IT! YOU TRULY ARE THE TRUE HERO. HYRULE IS SAVED!')
                return 'finished'
        
            else: 
                print('Kohga: You are no match for me!')
                print('Kohga swings the ball at you and you are crushed by a million spikes')
                print('Kohga: My greatness truly is radient')
                return 'death'

        if answer == '2':
            print('You take the flame blade and aim it at Master Kohga.')
            print('Kohga: Ha! Is that a flame blade I see?')
            print('Kohga: Well let\'s see how it does against this!')
            print('Kohga pulls out a water gun and sprays the flame blade.')
            print('The blade dries out and crumbles')
            print('Kohga: Poor child! Did you really think thay could stop the great Master Kohga!')
            print('Kohga proceeds to throw spiked balls at you. You eventually get crushed')
            return 'death'
       
class Death(Scene):
    
    def enter(self):
        print('You lose!')
        print("\nPaku: Nooo, he died! Now we'll have to eat bananas for the rest of our days * weeps for all eternity *")
        exit(1)

class Finished(Scene):

    def enter(self):
        print('Paku: You know, I never actually got to ask you. What is your true name hero?')
        name = input('>')
        print('\n')
        print ("You won! Good job.")
        
        print ('With the yiga clan destroyed, hyrule is now in peace again. All thanks to the true hero, {}'.format(name))
        return 'finished'


class Map(object):

    scenes = {
        'entrance': Entrance(),
        'transition': Transition(),
        'silent_forest': SilentForest(),
        'gorilla_room' :GorillaRoom(),
        'codeBreaker_room' : CodeBreaker(),
        'master_room' : MasterRoom(),
        'hyrule_castle' : HyruleCastle(),
        'secret_room' : SecretRoom(),
        'death' : Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('entrance')
a_game = Engine(a_map)
a_game.play()
