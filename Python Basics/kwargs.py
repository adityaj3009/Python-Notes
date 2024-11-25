# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword argument.

def my_function(**kwargs):
    for key, value in kwargs.items():
        print(str(key) + " = " + str(value))

my_function(name="John", age=30, country="USA", state="washington")