usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello admin, would you like to see a status report")
        else:
            print(f"Hello {username}, thenk you for logging in again")
else:
    print("We need some users")       