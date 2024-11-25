# Tuple = collection which is ordered and unchanageable
#         used to group together related data

student = ("Aditya", 19, "male")   #tuple of student
print(student.count("Aditya"))
print(student.index("male"))

for x in student:
    print(x)

if "Aditya" in student:
    print("Aditya is here")

#-----------------------------------------------------------------------------

# applying index operator

student = ("Aditya", 19, "male")

# Accessing elements using index operator
name = student[0]
age = student[1]
gender = student[2]

print(name)   # Output: Aditya
print(age)    # Output: 19
print(gender) # Output: male
