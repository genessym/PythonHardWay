# is - a // Animal is a object
class Animal(object):
    pass

# is - a // Dog is a object
class Dog(Animal):

    def __init__(self,name):
        ## has - a
        self.name = name

# is - a
class Cat(Animal):

    def __init__(self,name):
        # has - a
        self.name = name

# is - a
class Person(object):

    def __init__(self,name):
        # has - a
        self.name = name
        # Person has - a pet of some kind
        self.pet = None

# is - a 
class Employee(Person):

    def  __init__(self,name,salary):
        # has - a
        super(Employee,self).__init__(name)
        # has - a
        self.salary = salary

# is - a
class Fish(object):
    def __init__(self,name,water_preference):
        self.name = name
        self.water = water
        self.water_preference = water_preference

# is - a
class Salmon(Fish):
    def __init__(self,color):
        self.color = color

Billy = Fish('billy','salt water')
Nancy = Salmon('pink')

# is - a
class Halibut(Fish):
    def __init__(self,age):
        self.age = age

Rover = Halibut('3000 years old')

# is - a 
rover = Dog("Rover")

# is - a
satan = Cat("Satan")

# is - a
mary = Person("Mary")

# is - a 
mary.pet = satan 

# is - a
frank = Employee("Frank",120000)

# is - a
frank.pet = rover

# is - a
flipper = Fish()

# is - a
crouse = salmon()

# is a 
harry = Halibut()

# Study Drill:
# 2) Yes, everything in python is an oject. 




