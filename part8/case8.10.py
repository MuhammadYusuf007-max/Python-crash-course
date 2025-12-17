sent_messages = []
def send_messages(texts:list):
    for text in texts:
        print(text)
        sent_messages.append(text)

messages = ["hi", "okey", "mm"]
send_messages(messages)
print(messages, sent_messages)

