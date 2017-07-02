def add(a, b):
    print "ADDING %d + %d" % (a,b)
    return a + b

def subtract(a,b):
    print "SUBTRACTING %d - %d" % (a,b)
    return a-b

def multiply(a,b):
    print "MULTIPLYING %d * %d" % (a,b)
    return a * b
    
def divide(a,b):
    print "DIVIDING %d / %d" % (a,b)
    return a/b

print "Let's do some math with functions"

age = add(30, 5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."
#original formula
#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#new formula
what = age + (height - (weight * (iq / 2)))
print "That becomes:", what, "Can you do it by hand?"

#Study Drills:
def remainder (a,b):
    print "remainder of %d and %d:" %(a,b)
    return a % b

the_remainder = remainder(40,3)
print the_remainder

def split (a):
    print "I will split any number in half:"
    return a/2

splitter = float(raw_input(">"))
print split(splitter)



