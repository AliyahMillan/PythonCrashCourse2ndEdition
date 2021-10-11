"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
Sandwiches: Write a function that accepts several items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
"""

def make_sandwich(*items):
    print("\nI'll make you a Gio-style sandwich:")
    for item in items:
        print("---> Adding " + item + " to your sandwich.")
    print("Your sandwich is ready to eat!")

make_sandwich('ham', 'sharp cheddar cheese', 'lettuce', 'onions')
make_sandwich('turkey', 'light mayo', 'tomatoes')
make_sandwich('cheese', 'more cheese')
