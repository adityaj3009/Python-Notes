# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc)
#                   creates a zip object with paired elements stored in tuples for each elements

usernames = ["Aditya", "Adii"]     # list of username   (it can also be lists, sets...)
passwords = ("P@ssword", "abc123@")   # tuples of username (it can also be lists, sets...)
login_date = ["1/1/2021", "2/6/2023"]

users = (zip(usernames, passwords, login_date))
print(type(users))    # type - dict

for i in users:
    print(i)

print("-----------------------")

# convert to dict

users = dict(zip(usernames, passwords))
print(type(users))    # type - dict

for key,value in users.items():
    print(key+ "-" + value)

