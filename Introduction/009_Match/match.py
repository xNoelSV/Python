value = 10

# equivalent switch from Java in Python
match value:
    # Ten or eleven
    case 10|11: 
        print("OK")
    case 15:
        print("Warning")
    case _: #default
        print("Uknown code")