fruits = ("apple", "pear", "orange")
days = ("Mon", "Tue", "Wed")

for i, fruits in enumerate(fruits): # Iterate through fruits with index
    print(i, fruits)

for fruit, day in zip(fruits, days): # Iterate through fruits and days together using zip
    print(fruit, day)

