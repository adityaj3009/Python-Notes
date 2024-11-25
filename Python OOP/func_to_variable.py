def hello():
    print("hello")

print(hello)  # this will print the memory location
hi = hello
print(hi)     # this will get same memory location as hello

hi()

say = print
say("this can also print text")