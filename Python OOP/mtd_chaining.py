# method chaning = calling multiple method sequentially
#                  each call performs an action on the same object and return self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self
    
    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self

car = Car()
car.turn_on()
car. drive()

car.brake().turn_off()   # method chaining

# diff way for method chaining
print("------------------------------------------")
car.turn_on()\
.drive()\
.brake()\
.turn_off()