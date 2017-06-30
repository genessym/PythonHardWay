from sys import argv 

script, user_name , my_age = argv
prompt = '*'

print "Hi %s, I'm the %s script." %(user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "How old are you?"
age = int(raw_input(prompt))

print " Wow %d, you look so young. What's your secret" % age

print """
Alright, so you said %r about liking me. You live in %r. 
Not sure where that is. And you have a %r computer and you're 
only %d. Nice.
""" %(likes,lives,computer, age)