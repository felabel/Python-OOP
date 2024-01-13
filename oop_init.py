# The __init__ method is run as soon as an object of a class is instantiated (i.e. created). The method is useful to do any initialization (i.e. passing initial values to your object) you want to do with your object. Notice the double underscores both at the beginning and at the end of the name.

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# The previous 2 lines can also be written as
# Person('Swaroop').say_hi()


# how it works
# Here, we define the __init__ method as taking a parameter name (along with the usual self). Here, we just create a new field also called name. Notice these are two different variables even though they are both called 'name'. There is no problem because the dotted notation self.name means that there is something called "name" that is part of the object called "self" and the other name is a local variable. Since we explicitly indicate which name we are referring to, there is no confusion.

# When creating new instance p, of the class Person, we do so by using the class name, followed by the arguments in the parentheses: p = Person('Swaroop').

# We do not explicitly call the __init__ method. This is the special significance of this method.

# Now, we are able to use the self.name field in our methods which is demonstrated in the say_hi method.

