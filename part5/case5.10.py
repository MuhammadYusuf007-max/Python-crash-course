current_users = ["qwerty", "jonnikenidi", "admin", "Jonwik", "raj_kumar"]
current_users2 = [user.lower() for user in current_users]
new_users = ["qwerty", "jonniKenidi", "Isaknew", "ambulamagi", "mr_rupa"]
for user in new_users:
    if user.lower() not in current_users2:
        print(f"{user} is available in the list")

        