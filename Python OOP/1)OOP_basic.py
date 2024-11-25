# Class: A blueprint for creating objects, defining a set of attributes and methods.
# Object: An instance of a class containing data and behavior defined by the class.
# Instance: A specific object created from a class.
# Attribute: A variable that belongs to a class or an instance.
# Method: A function that belongs to a class and defines behaviors for its instances.
# Inheritance: A mechanism where a new class derives attributes and methods from an existing class.
# Encapsulation: The bundling of data and methods that operate on the data within one unit (class), restricting direct access to some of the object's components.
# Polymorphism: The ability to present the same interface for different underlying forms (data types).
# Abstraction: The concept of hiding the complex implementation details and showing only the necessary features of an object.
# Constructor: A special method __init__ that is called when an instance of a class is created, used to initialize the object.

class Car:
    
    def __init__(self, make, model, year, color):
        self.make = make           # instance variable
        self.model = model         # instance variable
        self.year = year           # instance variable
        self.color = color         # instance variable

    def drive(self):
        print("This",self.model,"is driving")
    
    def stop(self):
        print("This",self.model," is stopped")

car_1 = Car("Chevy", "corvette", 2021,"blue")   # car_1 is object
car_2 = Car("Ford", "Mustang",2022, "red")

print(car_1.make,"__" ,car_2.make)
print(car_1.model, "__", car_2.model)
print(car_1.year, "__", car_2.year)
print(car_1.color, "__" ,car_2.color)

car_1.drive()
car_1.stop()

car_2.drive()
car_2.stop()





