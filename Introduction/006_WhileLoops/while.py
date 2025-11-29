value = 0

while value < 5:
    value += 1
    
    #if value > 2:
    #    break
    
    if value == 3:
        continue
    
    print("While", value)
# Putting else in the final of the loop makes while to enter this final block when
#   the condition is no longer true. No so commonly used
else:
    print("Finished.")