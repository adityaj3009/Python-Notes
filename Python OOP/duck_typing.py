# duck typing = concept where the clas of an object is less important than the methods/ attribution
#               class type is not checked if minimum methods/attributes are present
#               "If it walk like a duck, and it quacks like a duck, then it must be a duck"

class Duck:

    def walk(Self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")
    

class Chicken:

    def walk(self):
        print("This chicken is walking")
    
    def talk(self):
        print("This chicken is clucking")
    
class Person():
      
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)  # it will too work 
                       # if you remove a attribute from chicken ex. walk it will show error




    

    