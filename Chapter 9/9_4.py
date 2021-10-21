"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
11 October 2021

Number Served: Start with your program from 9-1. Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. 
Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. 
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business.
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

restaurant = Restaurant("Pangi Delicacies", 'italian cuisine')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 200

print("Number served: " + str(restaurant.number_served))
restaurant.set_number_served(690)

print("Number served: " + str(restaurant.number_served))
restaurant.increment_number_served(1000)

print("Number served: " + str(restaurant.number_served))
