people = 15
cars = 20
buses = 75
trucks = 20
planes = 30

if cars > people:
    print "We should take the cars."

elif cars < people:
    print "We should not take the cars"
else:
    print "We can't decide"

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else: 
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses. "
else:
    print "Fine, let's stay home then" 

#Study Drills:

#1) Elif is similar to if where it takes a condition and if true, will
#enter the block of code. And else is used when the if condition is not True, running
# what is under else.

if planes >= buses:
    print "Let's take the plane"
elif planes <= buses:
    print "Let's take a bus"
else:
    print "Can't decide"

if trucks > cars:
    print "Yahoo"
elif trucks < cars:
    print "Yipee"
else:
    print "woohoo"