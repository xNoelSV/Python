def calculate_area(width, height, length = 1):
    return width * height * length

# in this case, naming parameters, we can put args wherever we want
area = calculate_area(width=2, length=6, heigh=3)
print(area)