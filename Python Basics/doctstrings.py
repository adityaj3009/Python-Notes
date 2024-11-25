# Doctstrings = these are string literals that appears right after the
#               definition of a function, method, class, or module

# Docstrings act as documentation for the class, module, and packages. 
# On the other hand, Comments are mainly used to explain non-obvious portions of the code.

def sqaure(n):
    '''Takes in a number n , returns the sqaure of n'''   #doctstring
    print(n**2)
sqaure(5)
print(sqaure.__doc__)  # this is use to print doctstring


# PEP 8 - this document gives coding conventions
#  for the Python code comprising the standard library in the main Python distribution.