class Car:
    # Class variable
    total_cars = 0

    def __init__(self, brand, model):
        # Instance variables
        self.brand = brand
        self.model = model

        # Updating the class variable
        Car.total_cars += 1

# Creating instances of the Car class
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")

# Accessing instance variables
print(f"Car 1: {car1.brand} {car1.model}")
print(f"Car 2: {car2.brand} {car2.model}")

# Accessing class variable
print(f"Total Cars: {Car.total_cars}")

# In this example:

# total_cars is a class variable, and it is shared among all instances of the Car class. It is used to keep track of the total number of cars.
# brand and model are instance variables, and they are specific to each instance of the Car class. They represent the brand and model of each individual car.
