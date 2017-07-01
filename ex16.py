# import the argv function from the sys package
from sys import argv

#unpacks argv and applies arguments to the two variables
script, filename = argv
# prints "we're goign to erase "file that is inputted"
print "We're going to erase %r." % filename
# prints the statement below
print "If you don't want that, hit CTRL-C (^C)."
# prints the statement below
print "If you do want that, hit RETURN."

# Asks for the user input while showing the character "?"
raw_input("?")

# prints the statement "opening the file..."
print "Opening the file..." 
# Opens the filename and allows us to write in - assigning all 
# to the variable target
target = open(filename,'w')

# Prints the statement below
print "Truncating the file. Goodbye!"

# Empties the file target
target.truncate()

# prints the statement below
print "Now I'm going to ask you for three lines."

# asks for users input
line1 = raw_input("line 1:")
# asks for users input
line2 = raw_input("line 2:")
# asks for users input
line3 = raw_input("line 3:")

# prints the statement below
print "I'm going to write these to the file"

target.write("%s\n%s\n%s\n" % (line1,line2,line3))
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# prints the state "And finally, we close it"
print "And finally, we close it"
# closes the file target
target.close()

#Study Drill:
# 'w' tells the file to open in write mode