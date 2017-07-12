# i = 0
# numbers = []

def my_function(i,x,y,numbers):
    while i < x:
        
        print ("At the top i is {}".format(i))
        numbers.append(i)

        i = i + y
        print ("Numbers now:", numbers)
        print ("At the bottom i is {}".format(i))

    print ("The numbers:")

    for num in numbers:
        print (num)

# Study Drills:
#1) Turning code into a function:
#numbers = []
#my_function(2,20,2,numbers)

#5) Rewrite with for loops and range instead:

def new_function(min,max,skip):
    for number in range(min,max,skip):
        print ("At the top i is {}".format(number))
        numbers.append(number)
        #min += 1
        print ("Numbers: ",numbers)
        print ("At the bottom i is {}".format(number))
    
    for number in numbers:
        print (number)

numbers = []
new_function(2,10,2)

# No, you do not need a incrementor when using range. If you added a incremementor, it doesn't seem to do anything. 
# The program runs just fine w/ or w/o.