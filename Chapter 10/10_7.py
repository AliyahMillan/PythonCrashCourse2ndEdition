"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 October 2021

Addition Calculator: Wrap your code from 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.
"""
print("Enter 'x' at any time to stop.\n")
while True:
  try:
     num1 = input("\nGive me a number: ")
     if num1 == 'x':
       break

     num1 = int(num1)

     num2 = input("Give me another number: ")
     if num2 == 'x':
        break

     num2 = int(num2)

  except ValueError:
    print("I said give me a number, mate.")

  else:
    sum = num1 + num2
    print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum) + ".")
