prompt = "\nEnter the name of pizza toppings"
prompt += "\n(Enter quit for quit ): "

message = ""
while message != "quit":
    message = input(prompt)
    if message != 'quit':   
        print(f"We are add {message}")
    