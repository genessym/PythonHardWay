class Parent(object):

   def shirt(self):
       print("I am wearing a red shirt today! I look great")
   
   def name(self):
       print("Hi, My name is Dinkleberg")

   def food(self):
       print("My favorite food is jello")
    


class Child(Parent):
    
    def name(self): 
        print("Hey! My name is Bob")

    def food(self):
        super(Child,self).food()
        

   
        
dad = Parent()
son = Child()

dad.shirt()
son.shirt()

dad.name()
son.name()

dad.food()
son.food()