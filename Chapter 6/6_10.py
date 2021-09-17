"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021

Favorite Numbers: Modify your program from 6-2 so each person can have more than one favorite number. For one person, give them three favorite number and for another give them two favorite numbers.  Then print each person’s name along with their favorite numbers.

"""

favourite_numbers = {
  'Henry': [42, 17],
  'James': [42, 39, 56],
  'Rob': [7, 12],
}

for name, numbers in favourite_numbers.items():
  print("\n", name.title(), " likes the following numbers:")
  for number in numbers:
    print("  ", str(number))
