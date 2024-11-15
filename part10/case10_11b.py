from pathlib import Path
import json

path = Path('favorite_nnumber.json')
contents = path.read_text()
number = json.loads(contents)

print(number)