vacation = {}
active = True

while active:
    name = input("What is your name? ")
    place = input("If you visit one place in the world, where would you go? ")
    
    vacation[name] = place
    
    response = input("would anyone want to answer? (yes/no) ")
    if response == 'no':
        active = False

for name, place in vacation.items():
    print(f"{name} want to visit {place}")

    