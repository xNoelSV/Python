# A set is an unordered collection of unique elements. Sets are mutable.
numbers = {1, 3, 6, 4} 
print(numbers)

for x in numbers: 
    print(x)

print(3 in numbers) # Return boolean

numbers.add(7) # adds a single item
print(numbers)

numbers.update([9, 8]) # add multiple items
print(numbers)

numbers.remove(8) # Remove number 8
print(numbers)

numbers.discard(8) # Remove but if don't exist, it doesn't throw a Traceback
print(numbers)

print(set([1, 2, 3])) # Parse to set
print({n for n in range(5, 8)}) # Creates a set from [5 to 8)