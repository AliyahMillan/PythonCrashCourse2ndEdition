"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
8 September 2021
"""

pizza_list = ['Cheese', 'Pepperoni', 'BBQ Chicken', 'Stuffed crust']
for i in range(len(pizza_list)):
  print ("I like", pizza_list[i],".")
print("\nI'm actually not that crazy about pizza, I'm sorry.\nIt's ok, but I've never really craved it.\nMy favourite kind would be cheese though. Golden, not brown.\n")

friend_pizzas = ['Cheese', 'Pepperoni', 'BBQ Chicken', 'Hawaiian']

print("My favourite pizzas are: ")
for i in range(len(pizza_list)):
  print(pizza_list[i])
print("\nMy friend's favourite pizzas are: ")
for i in range(len(friend_pizzas)):
  print(friend_pizzas[i])
