# Key difference between tuples: Lists are mutable (id doesn't change in operations)
fruits = ["apple", "orange", "grape"]

print(id(fruits))
fruits += ["melon"]
print(id(fruits)) # Same id

fruits.append("pear") # add new item, as Java

fruits.extend(["blueberry"]) # add array at the end of the list

fruits.insert(2, "kiwi") # We inserting "kiwi" at the secon position

fruits_tuple = tuple(fruits) # Parsing list to a tuple

fruits_list = list(fruits_tuple) # Parsing tuple to a list