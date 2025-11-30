stuff = ("Charles", 7, 8.2, True, False, "Cats")

print(stuff[2])

# We cannot edit a tuple, it's final
# stuff[2] = "Leaf"

# We can unpack values of a tuple into variables
name, num1, num2, boolean1, boolean2, animal = stuff

# We can use also variable length variables to unpack
person, num11, num22, *other = stuff
print(person, num11, num22, other)
print(type(other))

# we can make a tuple with a single value putting comma behind
animal1 = "cat",
print(animal1)
print(type(animal1))