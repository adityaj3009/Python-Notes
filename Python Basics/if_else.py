# if statements = a block of code that will execute if it's condition is true

age = int(input("how old are you? "))

if age == 100:
    print("You are century old")
elif age >= 18 and age < 50:
    print("you are an adult")
elif age < 0 :
    print("You haven't been born yet")
elif age > 50 and age < 99:
    print("You are old")
else:
    print("you are a child")