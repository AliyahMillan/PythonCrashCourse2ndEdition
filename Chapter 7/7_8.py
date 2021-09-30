"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 September 2021
"""
sandwich_order = ['nutella', 'ham and cheese', 'turkey on rye', 'tuna']

completed_sandwich = []

while sandwich_order:
  current_sandwich = sandwich_order.pop()
  print("I'm working on your " + current_sandwich + " sandwich.")
  completed_sandwich.append(current_sandwich)

print("\n")
for sandwich in completed_sandwich:
  print("I made your " + sandwich + " sandwich.")
  
