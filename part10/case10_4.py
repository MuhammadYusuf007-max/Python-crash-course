from pathlib import Path

peth = Path('C:/Users/User/Desktop/Python_crash_course/try_it_yourself/part10/guest.txt')
full_name = input("Please, enter your full name. ")
peth.write_text(full_name)


