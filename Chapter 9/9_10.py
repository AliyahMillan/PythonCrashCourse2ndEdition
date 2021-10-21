"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
13 October 2021

Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. 
Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

*********************************
This file is called main.py
*********************************
"""
from restaurant import Restaurant


pangiCuisine = Restaurant('pangi cuisine', 'italian food')
pangiCuisine.describe_restaurant()
pangiCuisine.open_restaurant()

"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
13 October 2021

Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. 
Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

*********************************
This file is called restaurant.py
*********************************
"""

class Restaurant():
  def __init__(self, name, cuisine_type):
    self.name = name.title()
    self.cuisine_type = cuisine_type
    self.number_served = 0
  def describe_restaurant(self):
    message = self.name + " serves the best " + self.cuisine_type.title() + "! Her Majesty said so herself!"
    print("\n" + message)
  def open_restaurant(self):
    message = self.name + " is open for business!! Grab your waiter or waitress and start ordering some noodles and whathaveyou."
    print("\n" + message)
  def set_number_served(self, number_served):
    self.number_served = number_served
  def increment_number_served(self, additional_served):
    self.number_served += additional_served
