"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
11 October 2021
"""

class Restaurant():

  def __init__(self, name, cuisine_type):
    self.name = name.title()
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    message = self.name + " serves the best " + self.cuisine_type.title() + "! Her Majesty said so herself!"
    print("\n" + message)

  def open_restaurant(self):
    message = self.name + " is open for business. Grab your waiter and start ordering some noodles and whathaveyou."
    print("\n" + message)

pd = Restaurant("pangi delicacies", 'italian cuisine')
print(pd.name)
print(pd.cuisine_type.title())

pd.describe_restaurant()
pd.open_restaurant()

françaisfood = Restaurant("Français Food", 'french food')
françaisfood.describe_restaurant()

habit = Restaurant('habit burger', 'burgers')
habit.describe_restaurant()
