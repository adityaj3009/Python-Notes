# list comprehension = a way to create a new list with less syntax
#                      can mimic certain lamda functions, easier to read
#                       1. list = [expression for item in iterable]
#                       2. list = [expression for item in iterable if condition]
#                       3. list = [expression if/else for item in iterable]

squares = []                     # create a empty list
for i in range(1,11):            # create a for loop
    squares.append(i * i)        # define what each loop iteration should be
print(squares)

squares = [i*i for i in range(1,11)]   # using list comprehension 1
print(squares)

print("---------------------------")

students = [100,90,80,70,60,50,40,30,20,10,0]

passed_students = list(filter(lambda x: x>= 60, students))
passed_students = [i for i in students if i >= 60]                   # using list comprehension 2
passed_students = [i if i >= 60 else "failed" for i in students]     # using list comprehension 3
print(passed_students)