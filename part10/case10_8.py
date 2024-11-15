from pathlib import Path

for file in ['cats.txt', 'dogs.txt']:
    path = Path(f'C:/Users/User/Desktop/Python_crash_course/try_it_yourself/part10/{file}')
    try:
        contests = path.read_text()
    except FileNotFoundError:
        print(f"We dont find {path}")
    else:
        print(contests)