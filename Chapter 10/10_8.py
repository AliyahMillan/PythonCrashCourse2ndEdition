"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 October 2021

Cats and Dogs: Make two files, cats.txt and dogs.txt. 
Store at least three names of cats in the first file and three names of dogs in the second file. 
Write a program that tries to read these files and print the contents of the file to the screen. 
Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. 
Temporarily rename each of your files, and make sure the code in the except block executes properly.  
Make sure an exception is caught for either file missing.

This is cats_and_dogs.py
"""
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
  print("\nReading file: " + '\033[1m' + filename + '\033[0;0m') #tried to make the filename bold (I don't think it worked :/ )
  try:
    with open(filename) as f:
      contents = f.read()
      print(contents)
  except FileNotFoundError:
    print("  File not found!")

##########################################Note that all code after this line is commented in order to prevent compiling errors.
##########################################Text within cats.txt and dogs.txt should be written without being commented out. 
##########################################(Uncomment cats.txt and dogs.txt in order to make the code work. Obviously they're stored in different files.)
######################################cats.txt#####################################################
"""
Matcha
Kitty Purry
Clawsie
""" 
#####################################dogs.txt#######################################################
"""
Sasha
Emma
Charles
"""
