# Declare a variable called x and assign it w/ "There are 10 types of people"
x = "There are %d types of people." %10

# Declare a variable called binary and assign it w/ the word "binary"
binary = "binary"

# Declare a variable called do_not and assign it w/ the word "don't"
do_not = "don't"

# Declare a variable called y and assign it w/ "Those who know binary and those who don't"
y = "Those who know %s and those who %s" %(binary, do_not)

# Prints the statement " There are 10 types of people "
print x 

# Prints the statement "Those who know binary and those who don't"
print y 

# Using a "all strings" string format operator, it prints the statement "I said: There are 10 types of people"
print "I said: %r" %x 

# Using a string format operator, it prints the statement "I also said: Those who know binary and those who don't"
print "I also said: '%s'." % y

# Declares a variable called hilarious and assigns a boolean value (False)
hilarious = False

# Declares a variable called joke_evaluation and assigns it the statement "Isn't that joke so funny?! %r"
joke_evaluation = "Isn't that joke so funny?! %r"

# Prints the values of hilarious and joke_evalution together: "Isn't that joke so funny?! False "
print joke_evaluation % hilarious 

# Declares the variable w and assigns it w/ the statement "This is the left side of..."
w = "This is the left side of..."

# Declares the variable w and assigns it w/ the statement "a string with a right side"
e = "a string with a right side"

# Using a string concatenation operator, you print "This is the left side of.... a string with a right side"
print w + e 

#Study Drills:
# 3) I'm pretty sure there are 6 places where a string is put inside another string 
# 4) Adding the variables w and e with + makes it a longer string because its a concatenation operator - joining the values of the variables together
