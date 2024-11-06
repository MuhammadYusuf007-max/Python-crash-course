from random import choice

series = [1,4,6,7,3,8,5,0,2,9,"a","b","c","d",'e']

lotto = ""
for _ in range(4):
    lotto += f"{choice(series)}"
print(f"Who has this lottery number {lotto}")

my_ticket = ""
times = 0
while my_ticket != lotto:
    my_ticket = ""
    times += 1
    for _ in range(4):
        my_ticket += f"{choice(series)}"
        
print(f"for find the lotto i need to try {times} and the lotto is {lotto}")