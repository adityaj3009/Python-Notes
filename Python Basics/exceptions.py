# exception = events detected during execution that interrupt
#              the flow of a program

try:
    numerator = int(input("Enter 1st number: "))
    denominator = int(input("Enter 2nd number: "))
    result = numerator/denominator
#   print(result)
except ZeroDivisionError as e:    # e is completely optional, it just shows our mistake
    print(e)
    print("you cannont divide by zero!!")
except ValueError as e:
    print(e)
    print("Enter only number please")
else:
    print(result)
finally:                # always at the end but not complusory
    print("This will always execute")
#except Exception:
#   print("Something went wrong")