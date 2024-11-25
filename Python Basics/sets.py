# set = collection which in unordered, unindexed. No duplicate value

utensils = {"fork", "spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes)

dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))      # different elements
print(utensils.intersection(dishes))    # same elements

for x in utensils:
    print(x)