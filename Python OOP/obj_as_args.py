class Car:

    color = None

def change_color(car, color):

    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Car()

change_color(car_1, "red")
change_color(car_2, "yellow")
change_color(car_3, "blue")
change_color(bike_1,"black")


# The reason there are no parentheses in the print statements for the color attribute of the car
#  objects is because color is not a method (a function defined within a class),
# but rather an attribute (a variable associated with an instance of a class).
print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)


