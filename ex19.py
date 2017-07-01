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

def largest (sumo1,sumo2):
    print """ Hello ladies & gentlemen, today we will be presenting
 the two greatest sumo wrestlers ever known to man fighting for the
 title of "largest sumo:"""
    print " Sumo1 ranking at %d pounds" % sumo1
    print " And sumo2 ranking at %d pounds\n" %sumo2


print "Do you know what the two largest sumo wrestlers weigh?"
largest (475, 512)

print "Do you know what the two largest sumo wrestlers weigh?"
sumo1w = raw_input("Sumo1 weighs:")
sumo2w = raw_input("Sumo2 weighs:")

print "Biggest sumos are: "
weight1 = 532
weight2 = 473
largest(weight1,weight2)

print "Biggest sumos still are:"
largest(423 + 124, 162 + 354)