# Length have default of 1
# Default arguments have to go to the final of the arguments
def calculate_area(width, height, length = 1):
    return width * height * length

area = calculate_area(2, 3)
print(area)