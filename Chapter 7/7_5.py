"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 September 2021
"""
prompt = "--> How old are you?"
prompt += "\n--> Enter 'done' when you're finished. \n"
while True:
  age = input(prompt)
  if age == 'done':
    break
  age = int(age)
######################
  if age < 3:
    print("--> You get in free!")
  elif age < 13:
    print("--> Your ticket costs $10.")
  else:
    print("--> Your ticket costs $15.")
