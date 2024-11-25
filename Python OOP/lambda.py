# lambda = function written in 1 line using lambda keyword
#          accept any number of arguments, but only has one expression.
#          (think of it as a shortcut)
#          (useful if needed for a short period of time, throw-away)

# lambda parameter:expression


double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z 

print("Double is:",double(8))
print("Multiply is:",multiply(4,6))
print("Addition is:",add(2,4,5))

print("-------------------------------")


full_name = lambda first, last: first + " " + last
print(full_name("Aditya", "Jalgaonkar"))

age_check = lambda age: True if age >= 18 else False
print(age_check(18))

print("-------------------------------")


dollar_t0_inr = lambda r: r*82.3
print("4 dollars =",dollar_t0_inr(4))


print("-------------------------------")

dollars = float(input("Enter the amount: "))

d_to_inr = lambda dollar: dollar*82.3
print(f"The value of {dollars:g} $ is {d_to_inr(dollars):.2f} INR")

# The :g format specifier removes trailing zeros after the decimal point, 
# so if the input is 3, it will display 3 instead of 3.0, and if the input is 3.4, 
# it will display 3.4.

