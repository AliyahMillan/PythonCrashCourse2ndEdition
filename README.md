# Python Crash Course 2nd Edition Solutions
223P Lab/Homework solutions (By Aliyah Alexis Millán)

This page will be updated frequently to include new solutions.
The solutions will be, of course, in Python.


<p align="center">
  <img src="https://user-images.githubusercontent.com/60375020/142698229-c0ea50bf-ad24-4548-8fa9-d7b629bf062c.jpg" />
</p>



# Chapter 2 

## 2_1.py:
Simple Message: Assign a message to a variable, and then print that message.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 August 2021
"""

name = "My name is Aliyah!"
print(name)
```
--------------------
## 2_2.py:
Simple Messages: Assign a message to a variable, and print that message. Then change the value of the variable to a new message, and print the new message.
```python

"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 August 2021
"""

book = "How many books should I read?"
print(book)
book = "I'll take the lot!"
print(book)
```
--------------------
## 2_3.py:
Personal Message: Use a variable to represent a person’s name, and print a message to that person. 

Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 August 2021
"""

eric = "Hello Eric, would you like to learn some Python today?"
print(eric)
```
-------------------
## 2_4.py:
Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 August 2021
"""

name = "Aliyah Millan!"
print(name.lower())

name = "Aliyah Millan!"
print(name.upper())

name = "Aliyah Millan!"
print(name.title())
```
--------------------
## 2_5.py:
Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks:

Albert Einstein once said, “A person who never made a mistake never tried anything new.”
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
25 August 2021
"""

#I exchanged the comma with a colon, since my quote is from a song lyric. I thought it was interesting.
name = "Alec Benjamin"
filler = "once said in his song 'If I Killed Someone For You':"
quote = '\n"You have to understand that\nThe one I killed is me"'
print(name.title(), filler, quote)
```
--------------------
## 2_6.py:
Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. 
Then compose your message and represent it with a new variable called message. Print your message.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
25 August 2021
"""

#I exchanged the comma with a colon, since my quote is from a song lyric. I thought it was interesting.
famous_person = "Alec Benjamin"
filler = "once said in his song 'If I Killed Someone For You':"
message = '\n"You have to understand that\nThe one I killed is me"'
print(famous_person.title(), filler, message)
```
--------------------
## 2_7.py:
Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
Make sure you use each character combination, "\t" and "\n", at least once.Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
26 August 2021
"""
#I exchanged the comma with a colon, since my quote is from a song lyric. I thought it was interesting.
famous_personbefore = "Alec Benjamin"
filler = ":"
message = '\n\t"You have to understand that\n\tThe one I killed is me"\n'
print(famous_personbefore.title(), filler, message)
#Now with the whitespaces
famous_person = " Alec Benjamin "
print(famous_person)
print(famous_person.lstrip())
print
print(famous_person.rstrip())
(famous_person.strip())
```
--------------------
## 2_8.py:
Number Eight: Write addition, subtraction, multiplication, and division operations that each result in the number 8. Be sure to enclose your operations in print() calls to see the results. You should create four lines that look like this:
print(5+3)
Your output should simply be four lines with the number 8 appearing once on each line.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
26 August 2021
"""

print(1+7)
print(9-1)
print(2*4)
print(16/2)
```
--------------------
## 2_9.py:
Favorite Number: Use a variable to represent your favorite number. Then, using that variable, create a message that reveals your favorite number. Print that message.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
26 August 2021
"""
fav_num = 0
message = "My favourite number is "
print(message, fav_num)
```
--------------------
## 2_10.py:
Adding Comments: Choose two of the programs you’ve written, and add at least one comment to each. If you don’t have anything specific to write because your programs are too simple at this point, just add your name and the current date at the top of each program file. Then write one sentence describing what the program does.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
26 August 2021
"""
#I've added comments using triple quotes and this '#' symbol.
name = "My name is Aliyah!"
print(name)
```
--------------------
## 2_12.py:
Starting with the following program,
```
from math import pi
r = 12
area = pi* r ** 2
print ("The are of a circle with radius",r,"is",area)
```
modify this program to display the circumference of the circle. 
Determine how to use the round function to limit the number of decimals displayed to two.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
26 August 2021
"""
from math import pi
r = 12
area = pi* r ** 2
print ("The area of a circle with radius",r,"is",area)

circ = round(2*pi*r)
print("The circumference of a circle with radius",r,"is", circ)
```
--------------------
# Chapter 3
## 3_1.py: 
Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
1 September 2021
"""
names = ['Dylan1', 'Dylan2', 'Destiny']
print(names[0])
print(names[1])
print(names[2])
```
--------------------
## 3_4.py:
Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
1 September 2021
"""

dinnerInvites = ['Alec Benjamin', 'Rian', 'Brendon Urie']
message = "You're invited to my exclusive dinner party,"

print(message, dinnerInvites[0],"!")
print(message, dinnerInvites[1],"!")
print(message, dinnerInvites[2],"!")
```
--------------------
