print("Cat" == "Cat")

# in this case, cat is before dog because lexicographical order (c before d) in unicode table
print("cat" > "dog")

# in this case, D is before c (uppercase)
print("cat" > "Dog")

# we can check order with ord("[letter]")
print(ord("c"))
print(ord("D"))


