numbers = [0, 1, 2, 3, 4, 5, 6]

numbers.remove(4) # Remove the 4 number (not the position)
print(numbers)

numbers.pop() # We remove the last position, as Java
print(numbers)

numbers.pop(1) # We remove position 1
value = numbers.pop(1) # We can store the deleted item
print(value, numbers)

del numbers[2] # This also remove by position 
print(numbers)

numbers.clear() # This clear whole list
print(numbers)
