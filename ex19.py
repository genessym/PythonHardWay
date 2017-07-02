# Creates a function that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # prints the statement "You have '20'cheeses!
    print "You have %d cheeses!" % cheese_count
    # prints the statement "You have 30 boxes of crackers!"
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # prints the statment "Man that's enough for a party!"
    print "Man that's enough for a party!"
    # prints the statement "Get a blanket" and skips
    # to the next line
    print "Get a blanket.\n"

# prints the statement below as is
print "We can just give the function numbers directly:"
# gives the value to the two arguments cheese_count and boxes_of_crackers
cheese_and_crackers(20, 30)

# prints the statement below as is
print "OR, we can use variables from our script:"
# assigns the value 10 to amount_of_cheeses
amount_of_cheese = 10
# assigns the value of 50 to amountof_crackers
amount_of_crackers = 50
# the value 10 and 50 assigned to cheese_count, boxes_of_crackers
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
# print the statement below as is 
print "We can even do math inside too:"
# 20 gets assigned to cheese_count & 11 assigned to boxes_of_crackers
cheese_and_crackers(10 + 20, 5 + 6)

# 100 gets assigned to amount_of_cheese and 1000 gets assigned to amount_of_crackers
cheese_and_crackers(amount_of_cheese + 100,amount_of_crackers + 1000)

def smores (graham_crackers, chocolate_bars):
    print "We have %d graham crackers" % graham_crackers
    print "And we have %d chocolate bars" % chocolate_bars
    print "Let's make some smores!!"

print "Printing numbers directly:"
smores (50,25)


print "\nAdding numbers:"
smores(10+20,30 + 40)

print"\nVariables:"
graham_crackers = 1000
chocolate_bars = 4000
smores(graham_crackers,chocolate_bars)

print "\n variables and adding:"
smores(graham_crackers +325, chocolate_bars + 375)

 #Raw input attempt
print ("\n")
graham = int(raw_input("How many graham crackers do we have?\n>"))
chocolate = int(raw_input("How many chocolate bars do we have?\n>"))
print ("We have %d graham crackers and %d chocolate bars.") % (graham,chocolate)
print "Let's make smores!"