"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
28 October 2021

11-3. Employee: Write a class called Employee. The __init__() method should take in a first name, a last name, and an annual salary, and store each of these as attributes. 
Write a method called give_raise() that adds $5,000 to the annual salary by default but also accepts a different raise amount.

Write a test case for Employee called test_employee.py. Write two test methods, test_give_default_raise() and test_give_custom_raise(). 
Use the setUp() method so you don’t have to create a new employee instance in each test method. Run your test case, and make sure both tests pass.

For problem 11-3, turn in only employee.py and test_employee.py.

This is employee.py
"""
class Employee():
  def __init__(self, f_name, l_name, salary):
    self.first = f_name.title()
    self.last = l_name.title()
    self.salary = salary

  def give_raise(self, amount=5000):
    self.salary += amount
