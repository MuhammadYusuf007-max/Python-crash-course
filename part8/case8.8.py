def make_album(name, album, songs_number=None):
    artist = {"name": name, "album": album,}
    if songs_number:
        artist["songs_number"] = songs_number
    return artist

while True:
    print("Please enter the informations")
    print("if you want to quit please enter q")
    
    name = input("Enter name of artist ")
    if name == "q":
        break
    
    album = input("Enter name of album ")
    if name == "q":
        break
    
    print(make_album(name, album))