class Animal:
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):     # method overriding
        print("This rabbit is eating a carrot")   # This will get more preference cause it had over-ride

rabbit = Rabbit()
rabbit.eat()
