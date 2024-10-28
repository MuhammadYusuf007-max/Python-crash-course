pet1 = {
    "pet": "dog",
    "name": "olabay",
    "owner": "Yusuf",
    "age":6
}
pet2 = {
    "pet": "cat",
    "name": "motosh",
    "owner": "Mubashshira",
    "age": 9
}
pet3 = {
    "pet": "sheep",
    "name": "ajdarko'z",
    "owner": "Qobiljon",
    "age": 2
}

pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"The owner of {pet['age']} years old {pet['pet']} is {pet['owner']} and it is named {pet['name']}")