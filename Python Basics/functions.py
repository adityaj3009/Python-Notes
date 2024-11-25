#function = A block of code which is executed only when its called
#            also known as invoking of a function
# The order of every arguments matter


def hello():
    print("hello")
hello()            #function call


#For 1 parameter 1 argument is required , for 2 parameter 2 argument is required and so on...
def hee(name):     # here "name" is parameter
    print("have a nice day")
hee("Aditya")  #here aditya is a argument


def name(first, last, age):
    print("hello"+" "+first+ " "+ last)
    print("you are "+ str(age) +" "+ "years old" )
name("Aditya","Jalgaonkar", 19)

def student(nav, branch, roll_no):
    print("hello " + nav + "your branch is "+ branch)
    print("Your roll no. is " + roll_no)
student("Aditya", "EXTC", "23104A0042")
