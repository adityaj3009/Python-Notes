#slicing = create a substring by extarcting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Aditya Jalgaonkar"

first = name[0:6]
print(first)

last = name[7:17]
print(last)

reverse = name[::-1]    #to reverse a string use ::-1
print(reverse)

website = "http://google.com"
slice = slice(7,-4)
print(website[slice])