"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
13 October 2021

Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in 9-4. 
Add an attribute called flavours that stores a list of ice cream flavours. 
Write a method that displays these flavours. Create an instance of IceCreamStand, and call this method.
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
    message = self.name + " is open for business!! Grab your waiter and start ordering some noodles and whathaveyou."
    print("\n" + message)
  def set_number_served(self, number_served):
    self.number_served = number_served
  def increment_number_served(self, additional_served):
    self.number_served += additional_served

class IceCreamStand(Restaurant):
  def __init__(self, name, cuisine_type='ice_cream'):
    super().__init__(name, cuisine_type)
    self.flavours = []

  def show_flavours(self):
    print("\nWe have the following flavours:")
    for flavor in self.flavours:
      print("- " + flavor.title())

WeIcedYourCreme = IceCreamStand('We Iced your Creme')
WeIcedYourCreme.flavours = ['cookie dough', 'mint chocolate chip', 'fudge', 'coconut',  'mini milk']

WeIcedYourCreme.describe_restaurant()
WeIcedYourCreme.show_flavours()
