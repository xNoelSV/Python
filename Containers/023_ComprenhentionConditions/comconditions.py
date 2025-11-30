words1 = ["it", "was", "the", "best", "of", "times"]

words2 = [w for w in words1 if len(w) > 3] # We applied a filter to store the word
print(words2)

# Create a new list where words longer than 3 characters are converted to uppercase, 
# while shorter words remain unchanged.
words3 = [w.upper() if len(w) > 3 else w for w in words1]
print(words3)

