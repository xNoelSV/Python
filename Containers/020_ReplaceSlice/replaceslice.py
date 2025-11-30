numbers = list((0, 1, 2, 3, 4, 5, 6, 7))

numbers[2:4] = (0, 0, 0, 0) # We're replacing from [2 to 4) 
print(numbers)

numbers[2:6] = [] # We replaced content from [2 to 6)
print(numbers)

numbers[1::2] = ["hello", "to", "you"] # We replaced from [1 every 1 jump (2 positions)
print(numbers)