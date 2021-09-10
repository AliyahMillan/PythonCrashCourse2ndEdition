"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
8 September 2021
"""
cube_list = [num ** 3 for num in range(1,11)] #Allows me to create a single-lined for loop for my list as I make the list itself.
for cube in cube_list:
  print(cube)
#Starting 4_10.py:
print("The first three items in the list are: ", cube_list[:3])
print("Three items from the middle of the list are: ", cube_list[3:6])
print("The last three items in the list are: ", cube_list[7:10])
