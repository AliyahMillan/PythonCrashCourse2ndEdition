"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 October 2021

Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. 
Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. 
Test your program by entering two numbers and then by entering some text instead of a number.
"""
try:
  num1 = input("Give me a number: ")
  num1 = int(num1)

  num2 = input("Give me another number: ")
  num2 = int(num2)

except ValueError:
  print("I said give me a number, mate.")

else:
  sum = num1 + num2
  print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum) + ".")
