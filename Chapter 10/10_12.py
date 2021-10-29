"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 October 2021

Multiple Exceptions:  Add to the following code such that no unhandled exceptions occur.  Look through https://docs.python.org/3/tutorial/errors.html for example code if you are not sure how to do this.

x=[1,2,3,4]
for i in range(0,3):
    try:
        if i == 0: print(y)
        elif i == 1: 5/0
        else: x[4]
#Multiple except blocks to handle Exceptions            
    except NameError:
        print("Variable not defined")
# Add handlers for other exceptions
# After exception handling, execution continues
print("execution continues")
"""

x = [1, 2, 3, 4]
for i in range(0, 3):
  try:
    if i == 0: print(y)
    elif i == 1: 5 / 0
    else: x[4]

  #Multiple except blocks to handle Exceptions
  except NameError:
    print("Variable not defined")

  # Add handlers for other exceptions
  except ZeroDivisionError:
    print("Can't divide by zero!")
  except  IndexError:
    print("Index is out of range!")
  # After exception handling, execution continues
  print("Execution continues.....")

"""
Division calculator 3 py file by the professor:
###################################################
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else: 

        print(answer)
"""
