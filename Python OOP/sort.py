# sort() method = used with lists
# sort() function = used with iterables
# Iterable is an object which can be looed over or iterated over 
# with the help of a for loop. Objects like lists, tuples, sets, dictionaries, strings, etc. are called iterables. 

# --------------------------------------------------------------------------------------------------------------------------------


students = ["Aditya", "Adii", "Shravani", "Lena"]
# students.sort(reverse=True)   # reverse = true print list in reverse alphabetical order
sorted_students = sorted(students, reverse=True)    # here students are iterables
# sorted_students is a list

for i in sorted_students:  # this will create sorted list
    print(i)


print("---------------------------------------------")

child = [("Aditya", "A", 18),   # list of tuples
         ("Adii", "c", 19),
         ("Shravani", "B", 12)]

grade = lambda grades:grades[1]   # this will sort by the grade A,B,C.......... [1] is the index
# child.sort(key=grade, reverse=True)
sorted_child = sorted(child, key=grade)

for i in sorted_child:
    print(i)


