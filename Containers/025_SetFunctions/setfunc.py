numbers1 = {2, 4, 6, 8, 9}
numbers2 = {2, 4, 1, 3, 5}

print(numbers1.union(numbers2)) # Union sets, mathematical op (1, 2, 3, 4, 6, 6, 8, 9)
print(numbers1.intersection(numbers2)) # Intersect sets (2, 4, 6)

print(numbers1.difference(numbers2)) # Print the difference of "numbers1" over "numbers2"
print(numbers2.difference(numbers1)) # Print the difference of "numbers2" over "numbers1"
print(numbers2.symmetric_difference(numbers1)) # Return the numbers that doesn't appear in one of both sets

print(({1, 2, 3}).issuperset({1, 2, 3})) # Contains same values, then superset
print(({1, 2, 3, 4, 5}).issuperset({1, 2, 3})) # Has same values than second set
print(({1, 2, 3}).issuperset({1, 2, 3, 4, 5})) # Second set has same values + some more, then first set is not superset

