try:
    with open("C:\\Users\\HP\\Desktop\\new.txt.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found!!")