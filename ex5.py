name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy." 
print "He's got %s eyes and %s hair." %(eyes,hair)
print "His teeth are usually %s depending on the coffee" % teeth

print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)

inch_converter = height * 2.54
pound_converter = weight / 2.2

#Study Drills:
#1 cm & kg converter
print "Zedshaws height (%d) in centimeters is %f "  %(height, inch_converter)
print "Zedshaws weight (%d) in kilograms is %f" % (weight, pound_converter)

#2 Trying out various python format characters
my_age = 19
my_weight = 354.2
my_grade = "A"
failing_grade = "f"

print "Yeah, she's %d. %i is pretty old." %(my_age,my_age) 
print "I should probably go on a diet, I weigh %f." % my_weight
print "Alphonce gave me an %c in the class." % my_grade
print "You got a %c too" % failing_grade

print "Billy Bob just turned %r the other day yet weighs %r pounds. It's probably beause he studies in his room all day hence why he got an %s in Mrs.Hutchinsons class." % (my_age,my_weight,my_grade)
print "The third season of AOT comes out in %d" % 2018