from random import choice

series = [1,4,6,7,3,8,5,0,2,9,"a","b","c","d",'e']

lotto = ""
for _ in range(4):
    lotto += f"{choice(series)}"
print(f"Who has this lottery number {lotto}")