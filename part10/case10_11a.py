from pathlib import Path
import json

f_number = input("Enter your favorite number ")

path = Path('favorite_nnumber.json')
contests = json.dumps(f_number)
path.write_text(contests)
