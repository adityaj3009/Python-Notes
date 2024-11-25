# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     the order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our fucntion receives


def hello(first, middle, last):
    print("hello " + first+ " "+ middle+ " "+ last)
hello( last="jalgaonkar",first="Aditya", middle="vinod")   # using keyword arguments

