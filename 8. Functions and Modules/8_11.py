def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Message Sent: {current_message}")
        sent_messages.append(current_message)

messages1 = ["This is a short message.", "I love Python.", "This is in a list."]
messages2 = []

send_messages(messages1.copy(), messages2.copy())

print (messages1)
print (messages2)