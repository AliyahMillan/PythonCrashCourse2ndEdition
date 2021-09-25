"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 September 2021
"""

number = input("Please give me a number: ")
number = int(number)

if number % 10 == 0:
  print(str(number) + " is a multiple of 10.")
else:
  print(str(number) + " isn't a multiple of 10.")
