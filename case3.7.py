print("Sorry, i can only invite two people")
guests = ['Toriq ibn Ziyod', 'Umar Muxtor', 'Yorqinjon domla', 'Sheyx Muhammad Sodiq', 
'Adolf Hitler', 'Yusuf Hajjoj']
print(f"Sorry, i can't invite {guests.pop()}")
print(f"Sorry, i can't invite {guests.pop()}")
print(f"Sorry, i can't invite {guests.pop()}")
print(f"Sorry, i can't invite {guests.pop()}")

print(f"I invite {guests[0]}")
print(f"I invite {guests[1]}")

del guests[0]
del guests[0]
print(guests)