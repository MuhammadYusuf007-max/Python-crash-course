from pathlib import Path

for file in ['cats.txt', 'dogss.txt']:
    path = Path(f'C:/Users/User/Desktop/Python_crash_course/try_it_yourself/part10/{file}')
    try:
        contests = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(contests)