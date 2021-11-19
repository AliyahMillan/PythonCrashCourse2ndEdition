"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
15 November 2021
Cubes: A number raised to the third power is a cube. 
Plot the first 5000 cubic numbers.  
Display the graph as a blue line.
"""
#start with importing, them define the values, then make sure they're graphed, then customise the graph
from matplotlib import pyplot as plt
x_values = list(range(5001))
cubes = [x**3 for x in x_values]
plt.scatter(x_values, cubes, edgecolor='blue', s=40)
#fontsize
plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
#5,000
plt.axis([0, 5100, 0, 5100**3])
plt.show()
