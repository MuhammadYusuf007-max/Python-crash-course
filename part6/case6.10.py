favorite_numbers = {
    "Islom": [5, 13],
    "Amirxon": [15, 25],
    "Qobiljon": [7, 11],
    "Mardonbek": [22,49],
    "Asl": [25, 17],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")