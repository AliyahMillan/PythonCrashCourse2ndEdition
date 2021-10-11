"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""

def make_shirt(size='large', message="\nMy name is 'OR1=1;--\nPrepare to die.\n"):

  print("\nI'm going to make a " + size + " t-shirt.")
  print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', "Please stay @ 127.0.0.1. Don't be 255.255.255.255.")
