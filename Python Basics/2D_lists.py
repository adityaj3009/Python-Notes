#2d list = list of list  OR multidimensional list

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "burger", "chicken"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]
print(food)
print(food[1])   # To print any 1 list
print(food[0][1])   # To print any 1 element of a list

for x in food:
    print(x)
