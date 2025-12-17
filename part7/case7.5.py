while True:
    age = int(input("How old are you? "))
    if age < 3:
        print("Ticket is free for you")
    elif age < 12:
        print("ticket price is 10$ for you")
    else:
        print("Ticket price 15$ for you")