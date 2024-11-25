# epoch = a date and time from which a computer measures system time
# The epoch is a reference point from which time is measured.

import time

print(time.ctime(0))  # this method will convert a time expressed in sec and convert it into a readable string
print(time.time())    # return current seconds since epoch

print(time.ctime())   # this print current date and time
print(time.ctime(time.time()))  # this too print current date and time

print("--------------------------------")

time_obj = time.localtime()
print(time_obj)
local_time = time.strftime("%B %d %Y %H : %M %S", time_obj)   # refer https://docs.python.org/3/library/time.html
print(local_time)

print("--------------------------------")

# to get UTC time or coordinated universal time
time_utc = time.gmtime()
print(time_utc)
local_time = time.strftime("%B %d %Y %H : %M %S", time_utc)   # refer https://docs.python.org/3/library/time.html
print(local_time)

print("--------------------------------")

time_str = "1 July, 2024"
time_object = time.strptime(time_str,"%d %B, %Y")
print(time_object)

print("--------------------------------")

# (year, month, day, hours, secs, day of week, day of year , dst)
# The time.asctime() function expects a tuple with 9 elements(not more)
time_tuple = (2024, 4, 20, 4, 20, 0, 0, 0, 0)
time_asc= time.asctime(time_tuple)
print(time_asc)

time_tuple = (2024, 4, 20, 4, 20, 0, 0, 0, 0)
time_asc= time.mktime(time_tuple)   # rtis convert everything in seconds
print(time_asc)


