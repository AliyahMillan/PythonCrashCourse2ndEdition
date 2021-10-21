"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
13 October 2021

Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.

Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint #Random integer

class Die():
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)

d6 = Die() #Made a 6 sided die
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("These are the 10 rolls of my 6-sided die:")
print(results)

d10 = Die(sides=10) #Made a 10-sided die
results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\nThese are the 10 rolls of my 10-sided die:")
print(results)

d20 = Die(sides=20) #Made a 20 sided die
results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\nThese are the 10 rolls of my 20-sided die:")
print(results)
