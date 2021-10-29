"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 October 2021

Silent Cats and Dogs: Modify your except block in10-8 to fail silently if either file is missing, but still print the names for the file that opens.
"""
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
  try:
    with open(filename) as f:
      contents = f.read()
  except FileNotFoundError:
    pass
  else:
    print("\nReading file: " + '\033[1m' + filename + '\033[0;0m') #I don't think the bold actually worked
    print(contents)
