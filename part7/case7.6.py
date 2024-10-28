prompt = "\nEnter the name of pizza toppings"
prompt += "\n(Enter quit for quit ): "

message = ""
while message != "quit":
    message = input(prompt)
    if message != 'quit':   
        print(f"We are add {message}")
   
active = True 
while active:
    age = int(input("How old are you(If you want to stop enter 0)? "))
    if age < 3:
        print("Ticket is free for you")
    elif age < 12:
        print("ticket price is 10$ for you")
    else:
        print("Ticket price 15$ for you")

while True:
    print("If you give me sentence I will repeat it. If you want to stop enter quit ")
    message = input()
    if message == 'quit':
        break
    