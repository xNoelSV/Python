days = {
    "Mon": "Monday",
    "Tue": "Tuesday",
    "Wed": "Wednesday",
    "Thur": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday"
}

del days["Mon"] # Deletes item
print(days)

print(days.pop("Thur")) # Deletes item and return its value
print(days)

print(days.popitem()) # Deletes item and return whole item
print(days)

days.clear()
days = {}