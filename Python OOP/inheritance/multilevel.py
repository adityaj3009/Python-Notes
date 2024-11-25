# multi-level inheritance = when a derived child class inherits another child class

class Organism:
    alive = True

class Animal(Organism):   # This is a parent class for class Dog AND subclass of class Organism
    def eat(self):
        print("This animal is eating")

class Dog(Animal):       # this inherits animal class
    def bark(self):
        print("This dog barks")

dog = Dog()
print(dog.alive)
dog.bark()
dog.eat()

animal = Animal()
animal.eat()
