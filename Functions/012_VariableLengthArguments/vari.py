def cataloge(name, *args):
    
    # this shows us the type of the variable we watching
    print("Type: ", type(args))
    
    print(name)
    
    if len(args) >= 1:
        print(args[0])
    
    for value in args:
        print(value)

cataloge("Trees", "oak", "ash", "linden")
cataloge("Blank")