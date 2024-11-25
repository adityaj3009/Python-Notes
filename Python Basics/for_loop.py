# for loop = a statement that will execute it's block of code
#             a limited amount of times
#
#             while loop = unlimited
#               for loop = limited

for i in range(10):
    print(i+1)

for i in range(50,100,2): # "2" will help in increment for eg. 92,94,96..
    print(i)

for i in "Aditya":
    print(i)

# ----------------------------------------------------------------------------------------------------

import time

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy new year")