ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there's not 10 things in that list, let's fix that.")
# Splits the list stuffs with '' in between them
#split(' ',stuff)
stuff = ten_things.split(' ')
more_stuff = ["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]

while(len(stuff)) != 10:
    # returns the word "boy" to next_one from list more_stuff
    #pop(more_stuff, ' ')
    next_one = more_stuff.pop()
    print ("Adding: ", next_one)
    # Adds next_one to the list stuff
    # append(stuff,next_one)
    stuff.append(next_one)
    print ("There's {} items now.".format(len(stuff)))

print ("There we go: ", stuff)

print ("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1])
print (stuff.pop())
# joins things with '' between stuff
# join(' ', stuff)
print (' '.join(stuff))
# join('#',stuff from ranges 3 - 4)
print ('#'.join(stuff[3:5]))

#Study guide:
# The relationship between dir (something) and class is that dir gives you all the attributes of an obj
# Class is like a template.