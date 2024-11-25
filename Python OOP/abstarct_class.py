# Prevents a user from creating an object of that class
# + compels a user to override abstact methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod    #abc is acroynm for abstract class

class Vehicles(ABC):

    @abstractmethod
    def go(self):
        pass

class Car(Vehicles):

    def go(self):
        print("You drive the car")

class MotorCycle(Vehicles):

    def go(self):
        print("You ride the motorcycle")
    
vehicle = Vehicles()
car = Car()
motorcycle = MotorCycle()

vehicle.go()
car.go()
motorcycle.go()
