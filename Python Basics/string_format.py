# str.format = optional method that gives users
#               more control when displaying output
# {} - known as format field
# Parameter: A variable in a function definition. Example: def func(animal):.
# Argument: A value passed to the function. Example: func("cow")


animal = "cow"
item = "moon"

print("the "+animal+" jumped over the " +item)
print("the {} jumped over the {}".format(animal,item))  # format using variables
print("the {} jumped over the {}".format("cow","moon"))  # format using values
print("the {0} jumped over the {1}".format(animal,item))  # positional arguments
print("the {animal} jumped over the {item}".format(animal="cow",item="moon"))  # keyword arguments

# str.format() method

text = "The {} jumped over the {}"
print(text.format(animal,item))


#----------------------------------------------------------------------------------------------------------------------------------------

name = "Aditya"

print("Hello my name is {}".format(name))
print("Hello my name is {0:10}. Nice to meet you".format(name))  # :10 adds extra padding and 0 means positional arguments
print("Hello my name is {:10}. Nice to meet you".format(name))  # :10 adds extra padding
print("Hello my name is {:<10}. Nice to meet you".format(name))  # To left align (there would be no visible change)
print("Hello my name is {:>10}. Nice to meet you".format(name))  # To right align
print("Hello my name is {:^10}. Nice to meet you".format(name))  # To center align

# -----------------------------------------------------------------------------------------------------------------------------------------

number = 100000.43535

print("The number pi is {:.2f}".format(number))  # to display first 2 digit after decimal
print("The number is {:,}".format(number))       #To add comma at thousands place
print("The number is {:b}".format(int(number)))        # To show binary representation of number 
print("The number is {:o}".format(int(number)))      # To show octal representation of number 
print("The number is {:X}".format(int(number)))       # To show hexadecimal representation of number 
print("The number is {:E}".format(number))         # To show scientific representation of number 



