from pathlib import Path

peth = Path('C:/Users/User/Desktop/Python_crash_course/try_it_yourself/part10/learn_python.txt')
contents = peth.read_text()

for line in contents.splitlines():
    print(line.replace("python", "C"))