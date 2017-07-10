people = 54
cats = 17
dogs = 80
# Added
hamsters = 45

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

if hamsters > people:
    print "So many hamsters! I could get use to this."

#Study Drills:
# 1) The if statement usually means: if this condition is True, do this. If not, skip.
# So what ever is in the if statement block, gets executed if the condition
# is true.

# 2) It needs to be indented four spaces cause that's python syntax...
# 3) It will not run if not indented
# 4) You can put any boolean expression in the if statement
# 5) If you change the initial variable, you must make the change everywhere

