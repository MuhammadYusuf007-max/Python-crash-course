def make_album(name, album, songs_number=None):
    artist = {"name": name, "album": album,}
    if songs_number:
        artist["songs_number"] = songs_number
    return artist

print(make_album("Sherali Jo'rayev", "Dilorom", 23))