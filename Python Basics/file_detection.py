import os

path = "C:\\Users\\HP\\Desktop\\folder"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("This is a directory")  
else:
    print("That location doesn't exist")
