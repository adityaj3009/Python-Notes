# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments.

def add(num1, num2):
    sum = num1 + num2
    return sum

print(add(1,2))   # here we can't add 3 or more arguments like print(add(1,2,4))
                  # to solve this issue we use *args

#--------------------------------------------------------------------------------------------------

def addition(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(addition(1,2,3))

# other method

def adds(*math):
    sum = 0
    math = list(math)
    math[0] = 0  # Set the first element to 0
    for i in math:
        sum += i
    return sum

print(adds(1, 2, 3, 4, 7))

#

def adds(*math):
    sum = 0
    math = list(math)
    first_element = math[0]  # Save the original first element
    math[0] = 0  # Set the first element to 0
    for i in math:
        sum += i
    sum += first_element  # Add the original first element back to the sum
    return sum

print(adds(1, 2, 3, 4, 7))  # This should output 17







