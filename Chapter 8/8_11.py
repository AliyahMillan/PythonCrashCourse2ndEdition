"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
Archived Messages: Start with your work from 8-10. Call the function send_messages() with a copy of the list of messages. After calling the function, print both of your lists to show that the original list has retained its messages.

"""
def show_messages(messages):
  print("Showing all messages:")
  for message in messages:
    print(message)

def send_messages(messages, sent_messages):
  print("\nSending all messages:")
  while messages:
    current_message = messages.pop()
    print(current_message)
    sent_messages.append(current_message)

messages = ["hullo pangi", "how are u?", "u. me. mash bros 2nite", "\U0001F633"]
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
