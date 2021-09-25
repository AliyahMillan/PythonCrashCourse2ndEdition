"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 September 2021
"""
prompt = "\nWhat topping would you like on your pizza?"
#+= (operator?) adds another value with the variable's value and assigns the new value to the variable, according to Stack Overflow:
prompt += "\nEnter the word 'done' when you're finished: \n"

while True:
  toppings = input(prompt)
 # != is 'not equal'
  if toppings != 'done': #my conditional statement
    print("I'll add " + toppings + " to your pizza.")
  else:
    break #ends the while loop
