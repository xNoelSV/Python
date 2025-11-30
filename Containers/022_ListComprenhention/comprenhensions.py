numbers = [i for i in range (0,5)] # Store the value of "i"
print(numbers)

numbers = [i**2 for i in range(0,5)] # Store the value of "i" to the power of 2
print(numbers)

animals1 = ["cat", "mouse", "dog", "badger"]

animals2 = [animal for animal in animals1] # Store every animal of "animals1" into "animals2"
print(animals2)

lengths = [len(animal) for animal in animals1] # Store length of every animal word into "animals2"
print(lengths)