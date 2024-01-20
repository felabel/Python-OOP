# class P:

#     def __init__(self, x):
#         self.x = x

#     @property
#     # getter
#     def x(self):
#         return self.__x

#     @x.setter
#     def x(self, x):
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
# p1 = P(-5)
# print(p1.x)

class Robot:
    def __init__(self, name, build_year, city):
        self.name = name
        self.build_year = build_year
        self.city = city

    @property
    def name(self):
        return self.__name

    @property
    def build_year(self):
        return self.__build_year

    @property
    def city(self):
        return self.__city

    @name.setter
    def name(self, value):
        self.__name = value

    @build_year.setter
    def build_year(self, value):
        self.__build_year = value

    @city.setter
    def city(self, value):
        self.__city = value

# Example usage:

robot = Robot("RoboBot", 2022, "TechCity")

print(robot.name)        
print(robot.build_year)  
print(robot.city)  

# We observe that the process of creating getters and setters involves repetitive patterns. It would be advantageous to employ generic getters and setters, as demonstrated in the following example. In this example we use the __getattr__ and __setattr__ special methods to manage your attributes.
# check for an example in genericAttr.py file
