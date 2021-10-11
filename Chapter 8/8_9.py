"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021

Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
"""

def show_messages(messages):
  for message in messages:
    print(message)

messages = ["hullo pangi", "how are u?", "u. me. mash bros 2nite", "\U0001F633"]
show_messages(messages)
