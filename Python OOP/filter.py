# filter() = creates a collection of elements from an iterable for which a function return
#
# filter(function, iterable)

friends = [("Aditya", 19),    # friends is iterable
           ("Adii", 18),
           ("shravani", 12)]

age = lambda data: data[1]>= 18   # age is a function

buddies = list(filter(age, friends))

for i in buddies:
    print(i)
    