# imports the argv function that holds the number of
# arguments passed to your script from the sys module
from sys import argv

# "Unpacks" argv and assigns all the arguments to the two variables
script, filename = argv

# Declares a variable called txt that opens the file the user inputs
txt = open(filename)

# Prints "Here's your file along with the filename inputted by user"
print "Here's your file %r:" % filename
# Prints the contents of the text file 
print txt.read()

# Prints the statement "Type the filename again:"
print "Type the filename again:"
# Asks user to input file name again and prints >
file_again = raw_input("> ")

# Declares a variable that opens file user inputted
txt_again = open(file_again)

# Prints the contents of the file chosen
print txt_again.read()

# Study Drill:
# Neither is really better, you get the same output regardless.

txt.close()
txt_again.close()
