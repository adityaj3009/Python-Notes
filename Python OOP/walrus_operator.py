# walrus operator   :=

# new to python 3
# assignment expression aka walrus operator
# assigns values to variable as part of a large expression

# happy = True
# print(happy)

print(happy := True)


#foods = list()
#while True:
#    food = input("what food do you like? : ")
#    if food == "quit":
#        break
#   foods.append(food)

foods = []
while (food := input("what food do you like? : ")) != "quit":
    foods.append(food)

for food in foods:
    print(food)

