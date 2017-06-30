# Study Drill
from sys import argv

script, name, sickness = argv

prompt = "~"

print "Hi, my name is:", script
print "And I will be your doctor today."
print "Lets get started right away, what is your name?", name
print "How old are you?"
age = int(raw_input(prompt))
print "Do you take any medications?"
medicationas = raw_input(prompt)
print "Okay, so I see here you've come here for:", sickness
print "How long has this been going on?"
time = raw_input(prompt)

print """
Well, my conclusion is your %d and you have %s.
You have had this for %s, the only answer it can be
is that you're dying. """ % (age,sickness,time)