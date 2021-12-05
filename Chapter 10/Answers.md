# Chapter 10: Exceptions
## 10_6.py:
**Addition:** One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. 
Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. 
Test your program by entering two numbers and then by entering some text instead of a number.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 October 2021
"""
try:
  num1 = input("Give me a number: ")
  num1 = int(num1)

  num2 = input("Give me another number: ")
  num2 = int(num2)

except ValueError:
  print("I said give me a number, mate.")

else:
  sum = num1 + num2
  print("The sum of " + str(num1) + " and " + str(num2) + " is " + str(sum) + ".")
```
## 10_7.py:
**Addition Calculator:** Wrap your code from 10-6 in a while loop so the user can continue entering numbers even if they make a mistake and enter text instead of a number.
 ```python
 """
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 October 2021
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
 ```
 ## 10_8.py:
**Cats and Dogs:** Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. 
 Write a program that tries to read these files and print the contents of the file to the screen. 
 Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. 
 Temporarily rename each of your files, and make sure the code in the except block executes properly.  
 Make sure an exception is caught for either file missing.
 ```python
 """
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 October 2021

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
  ```
_cats.txt:_
```
Matcha
Kitty Purry
Clawsie
```
_dogs.txt_
```
Sasha
Emma
Charles
 ```
 ## 10_9.py:
 **Silent Cats and Dogs:** Modify your except block in 10-8 to fail silently if either file is missing, but still print the names for the file that opens.
 ```python
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
``` 
 ## 10_10.py:
**Common Words:** Visit Project Gutenberg (https://gutenberg.org/ (Links to an external site.)) and find a few texts you’d like to analyze. 
Download the text files for these works, or copy the raw text from your browser into a text file on your computer.

Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. 
This count will be an approximation because of the way split() works.  To get a better idea of what split() is doing, print the list.  
Include an appropriate exception handler for file not found.

You can use the count() method to find out how many times a word appears in a list.  
 ```python
 """
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 October 2021 
"""
def count_common_words(filename, word): #324 is 'the' goal
  try:
    with open(filename, encoding='utf-8') as f:
      contents = f.read()
  except FileNotFoundError:
    pass
  else:
    word_count = contents.lower().count(word)
    msg = f"'{word}' appears in {filename} a total of {word_count} times."
    print(msg)

filename = 'HeyDiddleDiddleTXT.txt'
count_common_words(filename, 'the')
 ```
_Click this link to access HeyDiddleDiddleTXT.txt:_
 ```
 https://github.com/AliyahMillan/PythonCrashCourse2ndEdition/blob/962fd45eb07d1ef652b3920d257ba7f06b839d79/Chapter%2010/HeyDiddleDiddleTXT.txt
 ```
 
 
 
 
 
 
 
 
