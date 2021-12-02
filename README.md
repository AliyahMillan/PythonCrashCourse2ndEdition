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
## 3_5.py:
Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
 - Start with your program from 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
 - Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
 - Print a second set of invitation messages, one for each person who is still in your list.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
1 September 2021
"""
dinnerInvites = ['Alec Benjamin', 'Rian', 'Brendon Urie']
message = "You're invited to my exclusive dinner party,"

print("--->",message, dinnerInvites[0],"!")
print("--->",message, dinnerInvites[1],"!")
print("--->",message, dinnerInvites[2],"!")

print("\n--->\nRian to Aliyah:\n I'm so sorry, Aliyah, but I won't be able to make it to your dinner party. I don't own a tux and I can't imagine showing my face around your two idols without a tux. You'll have a great time without me anyways. Maybe next time we can just go to the library and try that new htb machine? Love you, sorry, have fun! :)")

print("\n<--->\nAliyah to Everyone:\n Hi everyone!", dinnerInvites[1],"chickened out and won't be able to make it to the party. :( I know you guys were all hoping to meet him, but... I expect you'll find our newest guest to be quite scintillating.\n")

dinnerInvites = ['Alec Benjamin', 'Brendon Urie', 'Stephen Colbert']

message = "You're invited to my exclusive dinner party,"

print("--->",message, dinnerInvites[0],"!")
print("--->",message, dinnerInvites[1],"!")
print("--->",message, dinnerInvites[2],"!")
```
## 3_6.py:
 More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
 - Start with your program from 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
 - Use insert() to add one new guest to the beginning of your list.
 - Use insert() to add one new guest to the middle of your list.
 - Use append() to add one new guest to the end of your list.
 - Print a new set of invitation messages, one for each person in your list.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
1 September 2021
"""

dinnerInvites = ['Alec Benjamin', 'Rian', 'Brendon Urie']
message = "You're invited to my exclusive dinner party,"

#Could turn this into a function or "for" loop
for i in range(len(dinnerInvites)):
  print("--->", message, dinnerInvites[i], "!")
""""
print("--->",message, dinnerInvites[0],"!")
print("--->",message, dinnerInvites[1],"!")
print("--->",message, dinnerInvites[2],"!")
"""
###################
print("\n--->\nRian to Aliyah:\n I'm so sorry, Aliyah, but I won't be able to make it to your dinner party. I don't own a tux and I can't imagine showing my face around your 2 idols without a tux. You'll have a great time without me anyways. Maybe next time we can just go to the library and try that new htb machine? Love you, sorry, have fun! :)")

print("\n<--->\nAliyah to Everyone:\n Hi everyone!", dinnerInvites[1],"chickened out and won't be able to make it to the party. :( I know you guys were all hoping to meet him, but... I expect you'll find our newest guest to be quite scintillating.\n")

dinnerInvites = ['Alec Benjamin', 'Brendon Urie', 'Stephen Colbert']

message = "You're invited to my exclusive dinner party,"

#Used a "for" loop to continuously print out my invites
for i in range(len(dinnerInvites)):
  print("--->", message, dinnerInvites[i], "!")
""""
print("--->",message, dinnerInvites[0],"!")
print("--->",message, dinnerInvites[1],"!")
print("--->",message, dinnerInvites[2],"!")
"""
###################

print("\n<--->\nAliyah to Everyone:\n Hey guys, great news! I managed to wrangle up a bigger dinner table, and I managed to convince Rian he can come back. The new table means there's also room for two more guests at our exclusive party.\n")

#Used a "for" loop to continuously print out my invites
dinnerInvites.insert(0, "Charlie Puth")
dinnerInvites.insert(2, "Rian")
dinnerInvites.append("Niall Horan")
#Used a "for" loop to continuously print out my invites
for i in range(len(dinnerInvites)):
  print("--->", message, dinnerInvites[i], "!")
""""
print("--->",message, dinnerInvites[0],"!")
print("--->",message, dinnerInvites[1],"!")
print("--->",message, dinnerInvites[2],"!")
print("--->",message, dinnerInvites[3],"!")
print("--->",message, dinnerInvites[4],"!")
print("--->",message, dinnerInvites[5],"!")
"""
```
## 3_7.py: 
Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
 - Use len() to print a message indicating the number of people you are inviting to dinner.
 - Add a new line that prints a message saying that you can invite only two people for dinner.
 - Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
 - Print a message to each of the two people still on your list, letting them know they’re still invited.
 - Use remove to remove the second to last name.  Use del to remove the last name from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
1 September 2021
"""

dinnerInvites = ['Alec Benjamin', 'Rian', 'Brendon Urie']
message = "You're invited to my exclusive dinner party,"
#Could turn this into a function or "for" loop
for i in range(len(dinnerInvites)):
  print("--->", message, dinnerInvites[i], "!")


print("\n--->\nRian to Aliyah:\n I'm so sorry, Aliyah, but I won't be able to make it to your dinner party. I don't own a tux and I can't imagine showing my face around your 2 idols without a tux. You'll have a great time without me anyways. Maybe next time we can just go to the library and try that new htb machine? Love you, sorry, have fun! :)")

print("\n<--->\nAliyah to Everyone:\n Hi everyone!", dinnerInvites[1],"chickened out and won't be able to make it to the party. :( I know you guys were all hoping to meet him, but... I expect you'll find our newest guest to be quite scintillating.\n")

dinnerInvites = ['Alec Benjamin', 'Brendon Urie', 'Stephen Colbert']
message = "You're invited to my exclusive dinner party,"

#Used a "for" loop to continuously print out my invites
for i in range(len(dinnerInvites)):
  print("--->", message, dinnerInvites[i], "!")

print("\n<--->\nAliyah to Everyone:\n Hey guys, great news! I managed to wrangle up a bigger dinner table, and I managed to convince Rian he can come back. The new table means there's also room for two more guests at our exclusive party.\n")

#Used a "for" loop to continuously print out my invites
dinnerInvites.insert(0, "Rian")
dinnerInvites.insert(2, "Niall Horan")
dinnerInvites.append("Charlie Puth")
#Used a "for" loop to continuously print out my invites
for i in range(len(dinnerInvites)):
  print("--->", message, dinnerInvites[i], "!")

print("\n~~~~~~~~~~~~~~ There are", len(dinnerInvites), "people who are invited to this dinner. ~~~~~~~~~~~~~~")
print("\n<--->\nAliyah to Everyone:\n Sadly, due to the fact that this is an 'exclusive' dinner party (and because my new dinner table won't arrive in time for the dinner), I've consulted my council of advisers, and they recommend to invite only two people to the dinner! This means that the two people who treated me best this month are now the only invitees to this dinner party! You will each receive a message that will tell you if you are invited or not. May the odds be ever in your favour!")
#####
message2 = "\n---> I'm so sorry, but it has been determined that you're ineligible to attend this dinner. Please try again next time,"
for i in range(len(dinnerInvites)-2):
  print(message2, dinnerInvites.pop(), "!") #This was also a new change

###notes to help me with loops and pop:
"""
list['']
print(list.pop())
#######
for person in list:
  person.pop(-1)
  print(message + whatnot)
"""
message3 = "\n---> Congratulations, you're still invited to the party, "
for i in range(len(dinnerInvites)):
  print(message3, dinnerInvites[i], "!")

print("\n\n")

dinnerInvites.remove(dinnerInvites[1])
print("After remove: ", dinnerInvites)
del dinnerInvites[0]
print("After del: ", dinnerInvites)
```
## 3_8.py:
Seeing the World: Think of at least five places in the world you’d like to visit.  For this program, format the output nicely to indicate what the operation is.  Also, include a brief comment in your code to indicate the intent of the operation.
 - Store the locations in a list. Make sure the list is not in alphabetical order.
 - Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
 - Use sorted() to print your list in alphabetical order without modifying the actual list.
 - Show that your list is still in its original order by printing it.
 - Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
 - Show that your list is still in its original order by printing it again.
 - Use reverse to change the order of your list. Print the list to show that its order has changed.
 - Reestablish your original list.
 - Use a combination of remove() and sorted() to remove the alphabetically first occurring value.  In the case of a list of animals, Aardvard is likely to be removed.  Print the list to show that its order has not changed.
 - Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
 - Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
3 September 2021
"""
#Storing the places I want to visit into a list, in non-alphabetical order:
places = ['England', 'France', 'Japan', 'Russia', 'Greece', 'Italy']
#Printing this original as a raw python list:
print("\nOriginal: ", places)
#Printing the list in alphabetical order:
print("\nIn alphabetical order: ", sorted(places))
#Showing the list remains unchanged, and that sorted() was temporary
print("\nOriginal: ", places)
#Printing the list in reverse alphabetical order:
print("\nIn reverse alphabetical order: ", sorted(places, reverse=True))
#Showing that the list remains unchanged, and that the list is no longer in reverse alphabetical order:
print("\nOriginal: ", places)
#Printing the list in reverse:
places.reverse
print("\nIn reverse: ", places)
#Turning the list back into its original form by reversing twice:
places.reverse
print("\nBack in its original form: ", places)
####################################################
"""
Use a combination of remove() and sorted() to remove the alphabetically first occurring value.  In the case of a list of animals, Aardvard is likely to be removed.  Print the list to show that its order has not changed.
"""
sorted(places)
del  places[0]
print("\nIn alphabetical order: ", places)
print("\nOriginal: ", places)
####################################################
#Store the list in alphabetical order
print("\nStoring the list in alphabetical order: ")
places.sort()
print(places)
#Store the list in reverse alphabetical order
print("\nStoring the list in reverse alphabetical order: ")
places.sort(reverse=True)
print(places)
```
## 3_11.py: 
Slicing: Suppose that word = "image" and phrase = "protein synthesis" write a program that displays the following string slices, i, age, im, iae, rote, protein synth, protein image.  The first line has been completed for you as an example.  Name the program string_slicing.py.
```python
# Provided Code
word[0]: i
```
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
2 September 2021
"""
word = "image"
phrase = "protein synthesis"

print(word[0])
print(word[2:5])
print(word[0:2])
print(word[0] + word[2] + word[4])
print(phrase[1:5])
print(phrase[0:13])
print(phrase[0:8] + word)
```
# Chapter 4
## 4_1.py:
Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

 - Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
 - Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 September 2021
"""

pizza_list = ['Cheese', 'Pepperoni', 'BBQ Chicken']
"""
print(' '.join(map(str, pizza_list)))
print("In a downward list:")
print('\n'.join(map(str, pizza_list))) #Accomplishes the same thing as a for loop
"""
#For loop:
for i in range(len(pizza_list)):
  print ("I like", pizza_list[i],".")
print("I'm actually not that crazy about pizza, I'm sorry.\nIt's ok, but I've never really craved it.\nMy favourite kind would be cheese though. Golden, not brown.")
```
## 4_3.py:
Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 September 2021
"""

num = list(range(1, 21))
for number in num:
  print(number)
```
## 4_4.py:
One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 September 2021
"""
#1M = 1,000,000
num = list(range(1, 1_000_001))
for number in num:
  print(number)
```
## 4_5.py:
Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 September 2021
"""
num = list(range(1, 1000001))

print(min(num))
print(max(num))
print(sum(num))
```
## 4_6.py:
Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 September 2021
"""
#Formula to follow: range([start], end, [step])
#where step is how many number jumps you are making
for i in range(1, 20, 2):
  print(i)
```
## 4_8.py:
Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 September 2021
"""

cube_list = []
for num in range(1, 11):
  cube = num**3
  cube_list.append(cube)

for cube in cube_list:
  print(cube)
```
## 4_9.py:
Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
8 September 2021
"""
cube_list = [num ** 3 for num in range(1,11)] #Allows me to create a single-lined for loop for my list as I make the list itself.
for cube in cube_list:
  print(cube)
```
## 4_10.py:
Slices: Starting with program 4-9, add several lines to the end of the program that do the following:
 - Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
 - Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
 - Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
```python
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
```
## 4_11.py:
My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
 - Add a new pizza type to the original list.
 - Add a different pizza type to the list friend_pizzas.
 - Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
```python
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
```
## 4_13.py:
Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
 - Use a for loop to print each food the restaurant offers.
 - Try to modify one of the items, and make sure that Python rejects the change.
 - The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
8 September 2021
"""
menuItems = (
  'Mac n cheese', 'Chicken nuggets', 'Cheeseburgers',
  'Lasagne', 'Fish n chips',
)

print("Here's your menu!:")
for item in menuItems:
 print("- ", item)

menuItems = (
  'Mac n cheese', 'Chicken nuggets', 'Cheeseburgers',
  'Spaghetti', 'Haggis', 
)

print("\nWe updated our menu!")
print("Here's the new menu:")
for item in menuItems:
  print("- ", item)
```
## 4_14.py:
_Trusted Users:_
 - Create a list called all_users and initialize it with three users.  Print it.
 - Add a user to this list using append
 - Create a list called untrusted_users with two users, one in all_users and one that is not.  Print it.
 - Using the two previously created lists, create a list called trusted_users 
     - using a list comprehension
     - using a for loop
     
_Sets_
 - Create a set called all_user with 5 user names.
 - Create a set called untrusted_users containing 2 users, one in all_users and one not in all_users.
 - Using subtraction, create a set called trusted users which contains all_users but none in untrusted_users.
 
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
8 September 2021
"""
"""
Create a list called all_users and initialize it with three users.  Print it.
Add a user to this list using append
Create a list called untrusted_users with two users, one in all_users and one that is not.  Print it.
Using the two previously created lists, create a list called trusted_users 
using a list comprehension
using a for loop

Sets
Create a set called all_user with 5 user names.
Create a set called untrusted_users containing 2 users, one in all_users and one not in all_users.
Using subtraction, create a set called trusted users which contains all_users but none in untrusted_users.

"""
#Lists:
all_users = ['User1', 'User2', 'User3']
print("Original list: ", all_users)

all_users.append('User4')
print("After append: ", all_users)

untrusted_users = ['User1', 'UserUntrust']
print("Untrusted users list: ", untrusted_users)

#sets:
all_users = {'Rian', 'Josiah', 'Aaron', 'Mathias', 'Aliyah'}
untrusted_users = {'Yao', 'Rian'}
trusted_users =  all_users - untrusted_users
print("All users: ", all_users,"\nTrusted Users: ", trusted_users)
```
## 4_15.py:
Sieve of Eratosthenens: Using only a python list, for, in, if, range and remove, write a program that will determine prime numbers between 2 and 1000.  

 - List the integers beginning with 2.
 - Circle 2 (it must be a prime).
     - Cross out all its multiples.  They cannot be primes.
 - Circle the next integer that is not yet crossed out
     - Cross out its multiples.
 - Repeat.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
8 September 2021
"""
#Done with help with Professor Graham
MAX_PRIMES = 1000
primes = list(x for x in range(2, MAX_PRIMES+1))
for current_prime in primes:
  for prime_multiple in range(current_prime*2, MAX_PRIMES*2, current_prime):

    #print(prime_multiple)
    if prime_multiple in primes:
      primes.remove(prime_multiple)

print(primes)
print("Length: ",len(primes))
```
# Chapter 5
## 



