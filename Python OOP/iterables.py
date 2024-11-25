#  An iterable is an object that can be iterated over,
#  meaning it can be looped through one element at a time.

# Here are some examples of iterables:
#
# Lists: [1, 2, 3, 4, 5]
# Tuples: (1, 2, 3, 4, 5)
# Strings: "hello"
# Dictionaries: {"a": 1, "b": 2, "c": 3}
# Sets: {1, 2, 3, 4, 5}
# Generators: (x**2 for x in range(5))
# Files: open("example.txt", "r")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Alternatively, you can use the iter() function to create
# an iterator object from an iterable:

fruits = ["apple", "banana", "cherry"]
iterator = iter(fruits)
print(next(iterator))  # "apple"
print(next(iterator))  # "banana"
print(next(iterator))  # "cherry"