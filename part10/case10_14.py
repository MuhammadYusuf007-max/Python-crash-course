from pathlib import Path
import json

information = {}

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def get_new_username(path):
    username = input("what is your name? ")
    while True:
        try:
            age = int(input("How old are you? "))
            break
        except:
            print("Please enter number.")
    country = input("Where are you from? ")
    information['username'] = username
    information['age'] = age
    information['country'] = country
    contents = json.dumps(information)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        name = input("Please enter your name. ")
        if name == username['username']:
            print(f"Welcome back, {username['username']}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}")
        
greet_user()