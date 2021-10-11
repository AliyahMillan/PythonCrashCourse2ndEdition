"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021

Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
**************************************
This file is called printing_models.py
**************************************
"""

import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)


"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021

Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
******************************************
This file is called printing_functions.py
******************************************
"""

def print_models(unprinted_designs, completed_models):
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)
        
def show_completed_models(completed_models):
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)
