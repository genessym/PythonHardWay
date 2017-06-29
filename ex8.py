# Declaring a variable named formatter that holds 4 string format placeholders
formatter = "%r %r %r %r"

# Prints the variable formatter substituting w/ 1 2 3 4
print formatter % (1,2,3,4)

# Prints the variable formatter substituting w/ "one" "two" "three" "four"
print formatter % ("one","two","three","four")

# Prints the variable formatter substituting w/ True False False True
print formatter % (True, False, False, True)

# Prints the variable formatter which ends up being '%r %r %r %r' printed
#four times
print formatter % ( formatter, formatter, formatter, formatter)

# Prints the variable formatter substituting w/ " I had this thing. That
# you could type up right. But it didn't sing. So I said goodnight."
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# The output uses both single and double quotes because in the statement 
# "But it didn't sing" has the ' in don't 