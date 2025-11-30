animals = ("cat",   "dog",    "giraffe",   "lion",    "elephant",     "badger")
#         0 | -6,   1 | -5,     2 | -4,    3 | -3,      4 | -2,        5 | -1

print(animals[2])
print(animals[1:4]) # from [1 to 4)
print(animals[-1]) # last
print(animals[-4: -1]) # from [-4 to -1)
print(animals[1:-1:2]) # from [1 to -1) jumping 1 (2 positions)
print(animals[:3]) # from [0 to 3)
print(animals[::2]) # from [o to last] jumping 1 (2 positions)
print(animals[::]) # entire tuple
