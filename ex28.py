import math
# (True and True) == True
# (False and True) = False 
# (1 == 1 and 2 == 1) == False
# ("test" == "test") == True
# (1 == 1 or 2 != 1) == True
# (True and 1 ==1 ) ==  True
# (False and 0!=0) == False
# (True or 1 == 1) == True
# ("test" == "testing") == False
# (1 != 0 and 2 == 1) == False
# ("test" != "testing") == True
# ("test" == 1) == False
# not (True and False) == True
# not (1 == 1 and 0 != 1) == False  (got this wrong - right answer : true)
# not (10 == 1 or 1000 == 1000) == False
# not (1 != 10 or 3 == 4) == False
# not ("testing" == "testing" and "Zed" == "Cool guy") == True
# not 1 == 1 and (not ("testing" == 1 or 1 == 0)) == False
# "chunky" == "bacon" and (not( 3 == 4 or 3 == 3)) == False
# 3 == 3 and (not( "testing" == "testing" or "Python" == "Fun")) == False

# Got 19/20 right.

#Study Drills:
print True <= False
print not (1 == 1 or 1 < 3 (not (25 >= 2 and 3 != 3)))

name = raw_input("\nWhat\'s your name?")
if len(name) >= 5:
    print "Wow, that's long"
if len(name) <= 4:
    print "Wow, that's short"

if 5 == 3:
    print True
else: 
    print False

if (not(3 <= 4 or ("string" == "string" and 243 == 273))):
    print True
else: 
    print False

print "\n"
problem1 =  3 > 4 and 35293 <= 39274
problem2 = 5 != 7
problem3 = not (not ("Susy" >= "susy" and "hola" != "hola"))
print problem1
print problem2
print problem3