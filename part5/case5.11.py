ordinal_numbers = [i for i in range(1, 10)]
for i in ordinal_numbers:
    if i == 1:
        print("1st")
    elif i == 2:
        print("2nd")
    elif i == 3:
        print("3rd")
    else:
        print(f"{i}th")