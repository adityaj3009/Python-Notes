# Loop control statement = change a loops execution from its normal sequence

# break =        used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break
#------------------------------------------------------------

phone = "123-456-7890"
for i in phone:
    if i == "-":
        continue
    print(i, end="")

#----------------------------------------------------------------------------

for i in range(1,20):
    if i == 13:
        pass
    else:
        print(i)