# Assigning the value 100 to cars
cars = 100

# Assigning the value 4.0 to space_in_a_car
space_in_a_car = 4.0

# Assigning the value 30 to drivers
drivers = 30

# Assigning the value 90 to passengers
passengers = 90

# Subtracting the values of cars and drivers and assigning it to a new variable called cars_not_driven
# 100 - 30 = 70 
cars_not_driven = cars - drivers

# Assigning the same value of drivers to a new variable of cars_driven
# 30 == 30
cars_driven = drivers

# Multiplying the values of cars_driven and space_in_a_car into new variable carpool_capacity
# 30 * 4.0 = 120
carpool_capacity = cars_driven * space_in_a_car

# Dividing the values 90 / 30 and assigning 3 to new variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

#Prints the statement "There are 100 cars avaliable."
print "There are", cars, "cars available."

#Prints the statement "There are only 30 drivers avaiable."
print "There are only", drivers, "drivers available."

# Prints the statement "There will be 70 empty cars today."
print "There will be", cars_not_driven, "empty cars today."

# Prints the statement "We can transport 120 people today."
print "We can transport", carpool_capacity, "people today"

# Prints the statement "We have 90 to carpool today"
print "We have", passengers, "to carpool today"

# Prints the statement "We need to put about 3 in each car"
print "We need to put about", average_passengers_per_car, "in each car"

# Study Drills:
# The error in line 8 was due the extra underscore character between "car" and "pool". He misspelled the original variable that he had defined.

# Question 1: Whether you use 4 or 4.0 in this case, you get the same output
# Question 4: = is an assignment operator

x = 3