"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
15 November 2021
Colored Cubes: Apply a colormap to your cubes plot.
"""

from matplotlib import pyplot as plt
x_values = list(range(5001))
cubes = [x**3 for x in x_values]
#use cmap
plt.scatter(x_values, cubes, edgecolor='none', c=cubes, cmap=plt.cm.BuGn, s=40)
plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 5100**3])
plt.show()
