# f - string means to add variable to strings


letter = "Hey my name is {} and i am from {}"
country = "India"
name = "Aditya"

print(letter.format(name, country))
print(f"Hey my name is {name} and i am from {country}")

price = 49.09847
txt = f"For only {price:.2f} dollars!"   # .2f for printing just 2 decimals
print(txt)

print(type(f"{2*30}!!"))



