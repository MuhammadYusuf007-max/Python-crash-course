from pathlib import Path

peth = Path('C:/Users/User/Desktop/Python_crash_course/pg20023-images.txt')
contests = peth.read_text()
count = 0
for line in contests.splitlines():
    count += line.lower().count('the')
print(count)
