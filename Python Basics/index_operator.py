# index operator [] = gives access to a sequence's element (str, tuples, list)

name = "aditya Jalgaonkar!"

if(name[1].islower()):
    name = name.capitalize()
print(name)

first = name[0:7].upper()    # for [0:7] we can also write [:7]
print(first)

last = name[7:].lower()
print(last)

lasr_char = name[-1]
print(lasr_char)