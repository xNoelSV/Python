from collections import defaultdict

people = {
    "Bob": 42,
    "Sue": 53,
    "Noel": 22,
}

print(people.get("Noel")) # Retrive "Noel" value
print(people.get("Pau", 23)) # Retrive "Pau". If doesn't exist, return 23

days = defaultdict(str) # We assign type of values of this dictionary
days.update({"Mon": "Monday", "Tue": "Tuesday"})
print(days["Mon"]) # Return "Mon" value
print(days["Wed"]) # Return "Wed" or in its case "str" --> We assigned it in the defaultdict