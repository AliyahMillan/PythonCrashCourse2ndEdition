"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
Sending Messages: Start with a copy of your program from 8-9. Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. After calling the function, print both of your lists to make sure the messages were moved correctly.
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
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
