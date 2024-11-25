# list = used to store mutiple items in a single variable

food = ["pizza", "burger", "toast"]
print(food)
print(food[0])
print(food[0][0])   # Print the first letter of the first item in the list

food[1] = "sushi"
print(food)

food.append("icecream")
food.remove("toast")
food.pop()     #remove last element
food.insert(0,"cake")
food.sort()
# food.clear    #to clear whole list
print(food)


for x in food:
    print(x)
