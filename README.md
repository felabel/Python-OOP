# Object Oriented Programming in Python
Learning python classes and objects. Study notes and examples you may find helpful. Feel free to clone or reach out to contribute.

- OOP is organizing your program where you wrap data and functionality inside something called an object while procedurre-oriented way is designing our pprogram around functions(what we mostly do)
- Classes and objects are the two main aspect of object oriented programming
- Variables that belong to an object or class are referred to as [fields]. 
- Objects can also have functionality by using functions that belong to a class. Such functions are called [methods] of the class. 
- Collectively, the fields and methods can be referred to as the attributes of that class.

The Self

- Class methods have only one specific difference from ordinary functions - they must have an extra first name that has to be added to the beginning of the parameter list, but you do not give a value for this parameter when you call the method, Python will provide it. This particular variable refers to the object itself, and by convention, it is given the name self.
- Methods - oop_method.py
- The __init__ method - oop_init.py file

Classes And Object Variables

- The data part of the object is referrred to as the fields, there are 2 types - class and object variables;

- Class variables are shared, they can be accessed by all instances of that class. There is only one copy of the class variable and when any one object makes a change to a class variable, that change will be seen by all the other instances.

- Object variables are owned by each individual object/instance of the class. In this case, each object has its own copy of the field i.e. they are not shared and are not related in any way to the field by the same name in a different instance. An example will make this easy to understand


