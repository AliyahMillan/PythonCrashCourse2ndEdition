"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
10 November 2021

Favorite Number Remembered: Combine the two programs from 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Use the file that was created in 10-11 to avoid file open problems. Run the program twice to see that it works.
"""
import json

try:
  with open('fav_number.json') as f:
    number = json.load(f)
except FileNotFoundError:
  number = input("What's your favourite number? ")
  with open('fav_number.json', 'w') as f:
    json.dump(number, f)
  print("Thanks, I'll remember that.")
else:
  print("I know your favourite number! It's " + str(number) + ".")
##Wow this really doesn't work though if the input was a non-number, lol.