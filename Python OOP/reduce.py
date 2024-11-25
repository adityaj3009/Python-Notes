# reduce() = apply a function to an iterable and reduces it to a single cumulative value.
#             performs function on first two elements and repeats process until 1 value remains

# reduce(function, iterable)

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y: x+y, letters)
print(word)

print("-----------------------")

factorial = [6,5,4,3,2,1]
a = lambda x, y : x * y
result = functools.reduce(a, factorial)
print(result)

print("--------------------------------")

while True: 
   fact = lambda n: 1 if n == 0 else n*fact(n-1)
   n = int(input("Enter your number: "))
   re = fact(n)
   print(f"The factorial of {n} is {re}")
