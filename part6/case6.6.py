favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edwart": "rust",
    "phil": "python",
}
people = ["edwart", "jen", "Joseph"]
guests = favorite_languages.keys()
for person in people:
    if person in guests:
        print(f"Thank {person.title()} for taking poll")
    else:
        print(f"I invite {person} to take the poll")