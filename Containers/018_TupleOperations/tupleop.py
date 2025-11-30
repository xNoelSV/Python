fruits1 = "apple", "orange"
fruits2 = "banana", "grape"

print(fruits1 + fruits2) # Combine and create a new tuple
print(fruits1 * 3) # Repeat same tuple 3 times

print(id(fruits1)) # We can check inmemory id
fruits1 += fruits2
print(id(fruits1)) # Id has changed, it acts like a pointer

print(fruits1) # We combined 2 tuples