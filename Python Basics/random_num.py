import random

x = random.randint(1,6)
y = random.random()
print(y)

list =['rock', 'paper', 'scissors']
z = random.choice(list)
print(z)

cards = [1,2,3,4,5,6,7,8,9,'K','Q','J','A']
random.shuffle(cards)
print(cards)