print "Let's practice everything"
print 'You\'d need to know \'bout ecapes with \\ that do \n newlines and \t tabs.'

poem = """ 
\tThe lovely world 
with logic so firmly planted 
cannot discern \n the needs of love
nor comprehend passion from intuition 
and requires an explanation 
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# Created a function that takes on argument called started
def secret_formula(started):
    # declared a variable and assigned it the value of started input * 500
    jelly_beans = started * 500
    # declared a variable and assigned it the value of jelly_beans/1000
    jars = jelly_beans /1000
    # declared a variable and assigned it the value of jars/100
    crates = jars/100
    # returns the assigned values of the three variables 
    return jelly_beans, jars, crates 

# Starting point is appointed the value of 10000
start_point = 10000 
# Declares "new" variables and calls the secret_formula function with 10000 as the start point
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "Wed' have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
# Prints the statement below whilst using a string formatter to call on the function secret_formula
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# Another possiblity is just calling the function and "inputting" a number straight in
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(1000)

