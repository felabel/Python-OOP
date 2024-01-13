# classes/objects can have methods just like functions except that we have an extra self variable. 
class Person:
    def say_hi(self):
        print('Hi, I will be world class')

p = Person()
p.say_hi()
# The previous 2 lines can also be written as
# Person().say_hi()