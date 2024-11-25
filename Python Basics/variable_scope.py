# scope = The region that a variable is recognized
#          A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created

name = "Adii"  # Global scope

def display_name():
    name = "Aditya"  # Local scope (available only inside this function)
    print(name)  # Prints the local variable "Aditya"

display_name()  # Calls the function and prints "Aditya"

print(name)  # Prints the global variable "Adii"
