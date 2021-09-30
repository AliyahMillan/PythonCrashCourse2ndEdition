"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 September 2021
"""
sandwich_order = [
    'pastrami', 'ham and cheese', 'Rian-style turkey on rye', 'pastrami',
    'cold ice cream', 'pastrami', 'cheesy, cheesy with cheese']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

print("\n")
while sandwich_order:
    current_sandwich = sandwich_order.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made you a " + sandwich + " sandwich!")

