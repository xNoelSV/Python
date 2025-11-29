# **kwargs is more like HashMap in java
def details(name, **kwargs):
    print("Name", name)
    
    print(type(kwargs))
    print(kwargs)
    
    if "heigth" in kwargs:
        print("Heigth--", kwargs["heigth"])
    
    for key in kwargs:
        print(key, kwargs[key])
    
details("Noel", heigth=175, age=22)