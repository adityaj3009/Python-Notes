# nested loops = The "inner loop" will finish all of it's itrrations before
#                finishing one iteration of "outer loop"

rows = int(input("how many rows? "))
columns = int(input("how many columns? "))
symbols = input("enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbols, end="")  # end="" prevent moving from next line
    print()
