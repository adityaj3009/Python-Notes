# each child class has it unique attribute with parent class attributes
# child class can inherit parent class but not vice versa

class Animal:   # parent class
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print('This animal is sleeping')
 
class Rabbit(Animal):      # child class this will inherit everthing of parent class
    def run(self):
        print("This rabbit is running")

class Fish(Animal):
    def swim(self):
        print("This fish can swim")

class Hawk(Animal):
    def fly(self):
        print("This hawk can fly")

animal = Animal()
rabbit = Rabbit()   # object
fish = Fish()
hawk = Hawk()

if rabbit.alive == True:
    print(f"Rabit is alive? : {rabbit.alive}")

rabbit.run()
fish.swim()
hawk.fly()
hawk.sleep()   # parent class access
animal.eat()

