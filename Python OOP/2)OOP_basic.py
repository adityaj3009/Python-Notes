# instance variable are declared inside  constructor
# class variable are declared within a class but outside the constructor

class Employee:         # here language, salary are class attributes
    language = "Python"
    salary = 1200000


    def __init__(self):                   # dunder method(starts with "__" ) which would be autmoatically called
        print("I am creating a object")

    def getInfo(self):         # we should write self
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod     # becaue of this we can run function without "self"
    def greet():
        print("good morning")


aditya = Employee()    # aditya is a object
aditya.name = "Aditya"    # name is object attribute or this whole is an INSTANCE attribute
aditya.language = "JavaScript"             # instance variable has higer prefrence over class attribute
print(aditya.name, aditya.language, aditya.salary)

adii = Employee()    # adii is a object
adii.name = "Adii"
print(adii.name, adii.language, adii.salary)


