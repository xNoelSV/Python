# 5 not included
for i in range(5):
    print("For loop", i)
    
# We can make jumps in a loop iterations
# In this case, we're jumping every 2 numbers (ex: 4, 6, 8, ...)
for i in range(4, 10, 2):
    print("For loop", i)
    
# We can also jump forwards by putting -x in third parameter
for i in range(4, 0, -1):
    print("For loop", i)