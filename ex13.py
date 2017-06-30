from sys import argv

#script, first, second, third = argv

#print "The script is called:", script
#print "Your first variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

#Study Drills:
# 1) Getting the error "you need more than 3 values to unpack".
#It means you need 3 arguments in total for it to run

script, a, b, c, d = argv
e = raw_input("The name is:")

print "Hi, I'm the script but others call me:",script
print "Hi, I'm the first arg but others call me:", a
print "Hey, I'm the second arg but others call me:", b
print "Hey, I'm the third arg but others call me:", c
print "I'm the fourth arg but you can just call me:", d
print e
