number_people = input("How many people are in their dinner group? ")
number_people = int(number_people)

if number_people > 8:
    print("you have to wait for the table")
else:
    print("Your table is already ready")