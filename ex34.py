# Practice:
# animals = ['bear','python','peacock','kangaroo','whale','platypus']

# 1) The animal at 1 == python
# The animal at 1 is the second animal which is a python

# 2) The third animal == peacock
# The animal at 2 is the third animal which is a peacock

# 3) The first animal == bear
# The animal at 0 is the first animal which is a bear

# 4) The animal at 3 == kangaroo
# The animal at 3 is the fourth animal which is a kangaroo

# 5) The fifth animal == whale
# The animal at 4 is the fifth animal which is a whale

# 6) The animal at 2 == peacock
# The animal at 2 is the third animal which is a peacock

# 7) The sixth animal == platypus
# The animal at 5 is the sixth animal which is a platypus

# 8) The animal at 4 == whale
# The animal at 4 is the fifth animal which is a whale

animals = ['bear','python','peacock','kangaroo','whale','platypus']

for animal in range(len(animals)):
   print ("The animal at {} is a {}".format(animal,animals[animal]))


champ_power = ['mipha\'s grace','revali gale','daruk\'s protection','urbosa\'s fury']
tw_originals = ['stiles','scott','lydia','derek','alison','jackson']

print ("\nWhich champions power is the most useful?")
print ("""\nQuite debatable, each are extremely useful in their own way. {} always come in for the
clutch while {} is just handy in handing final blows. {} is great in defending yourself from guardians but 
then {} is just usuable in possibly every situtation.""".format(champ_power[0],champ_power[3],champ_power[2],champ_power[1]))
answer = input("\nThis is hard. What do you think?\n>")
print("\nInteresting choice, I'd probably go with revali's gale.")

print("\n")
for character in tw_originals:
    print (character)