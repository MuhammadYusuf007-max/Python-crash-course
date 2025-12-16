from pathlib import Path
import json
path = Path('favorite_nnumber.json')
if path.exists():
    path = Path('favorite_nnumber.json')
    contents = path.read_text()
    number = json.loads(contents)
    print(number)
else:
    f_number = input("Enter your favorite number ")
    contests = json.dumps(f_number)
    path.write_text(contests)   
    print('Your favorite number is stored') 