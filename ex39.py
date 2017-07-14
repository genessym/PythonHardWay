#Create a mapping of state to abbrev.
states = {
    'Oregon': 'OR',
    'Flordia': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#Create a basic set of states and some cities in them
cities = {
    'CA': 'San Fransico',
    'MI': "Detroit",
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities 
print ('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ",cities['OR'])

# print some states
print ('-' * 10)
print ("Michigan's abbreviation is: ",states['Michigan'])
print ("Flordia's abbreviation is: ",states['Flordia'])

# do it by using the state then cities dict
print ('-' * 10)
print ("Michigan has: ", cities[states['Michigan']])
print ("Florida has: ", cities[states['Flordia']])

# print every state abbreviation
print ('- ' * 10)
for state, abbrev in states.items():
    print ("{} is abbreviated {}".format(state,abbrev))

# print every city in state
print ('- ' * 10)
for city,abbrev in states.items():
    print ("{} is abbreviated {}".format(abbrev,city))

# now both in the same
print ('- ' * 10)
for state,abbrev in states.items():
    print ("{} state is abbreviated {} and has city {}".format(state,abbrev,cities[abbrev]))

print ('- ' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print ("Sorry, no Texas")

city = cities.get('TX', 'Does Not Exist')
print ("The city for the state 'TX' is: {}".format(city))

