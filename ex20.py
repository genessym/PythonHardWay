# imports argv function from sys package
from sys import argv
# unpacks argv and passes to the two variables
script, input_file = argv

# A function called print_all that holds one argument/parameter
def print_all(f):
    # reads file
    print f.read()
# A function called rewind that takes one argument/parameter
def rewind(f):
    # defaults to position 0
    f.seek(0)
# A function called print_a_line that takes two arguments
def print_a_line(line_count, f):

     print line_count, f.readline()
# Opens in the input_file and creates a file object called
#current_file
current_file = open(input_file)

# Prints statement below
print "First let's print the whole file:\n"

# uses print_all function, which will read current_file
print_all(current_file)

# prints the statement below
print "Now let's rewind, kind of like a tape."
 # defaults current_file to position 0
rewind(current_file)

# prints the statement "Let's print three lines:"
print "Let's print three lines:"

# assigns 1 to current_line
current_line = 1
# prints the current line we're one and what is written
# on line 1 in current_file
print_a_line(current_line,current_file)
 # increases current_line by 1 making it 2 now

current_line += 1
#prints the current line we're one and what is written
# on line 1 in current_file
print_a_line(current_line,current_file)
 # increases current_line by 1 making it 3 now

current_line += 1
#prints the current line we're one and what is written
# on line 1 in current_file
print_a_line(current_line,current_file)
