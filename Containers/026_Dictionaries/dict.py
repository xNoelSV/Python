# Dictionaries are equivalent to Map in Java (key -> value)
months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
}

print(months["Jan"]) # Finds by key

months["Apr"] = "April" # Add key "Apr" with value "April"

months.update({"May": "May", "Jun": "June"}) # adds multiple items

for month in months: # Find entire item
    print(month, months(month))

for month in months.key(): # Find the key of the item
    print(month, months(month))

for month in months.values(): # Find the value of that item
    print(month)

for month in months.items(): # We get tuple of each item
    print(month)

for abbrev, name in months.items(): # We store the key and value into different variables
    print(abbrev, name)

print("Jan" in months) # Return boolean if key exists