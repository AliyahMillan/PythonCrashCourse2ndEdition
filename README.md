# **Python Crash Course 2nd Edition Solutions**
                                  223P Lab/Homework solutions (By Aliyah Alexis Millán)

This page will be updated frequently to include new solutions.
The solutions will be, of course, in Python.


<p align="center">
  <img src="https://user-images.githubusercontent.com/60375020/142698229-c0ea50bf-ad24-4548-8fa9-d7b629bf062c.jpg" />
</p>



# Chapter 2: Variables and Simple Data Types
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
# Chapter 3: Lists
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
# Chapter 4: More Lists
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
#Done with help from Professor Graham
MAX_PRIMES = 1000
primes = list(x for x in range(2, MAX_PRIMES+1))
for current_prime in primes:
  for prime_multiple in range(current_prime*2, MAX_PRIMES*2, current_prime):

    #print(prime_multiple)
    if prime_multiple in primes:
      primes.remove(prime_multiple)

print(primes)
print("Length: ", len(primes))
```
# Chapter 5: If
## 5_8.py:
Hello Admin: Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
 - If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
 - Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
9 September 2021
"""
usernames = ['admin', 'user1', 'user2', 'user3', 'user4']
for name in usernames:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello", name, ", thank you for logging in again!")
```
## 5_9.py:
No Users: Add an if test to program from 5-8 to make sure the list of users is not empty.
 - If the list is empty, print the message We need to find some users!
 - Remove all of the usernames from your list, and make sure the correct message is printed.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
9 September 2021
"""
usernames = []

if usernames:
  for name in usernames:
      if name == 'admin':
        print("Hello admin, would you like to see a status report?")
      else:
        print("Hello ", name, ", thank you for logging in again!")
else:
  print("We need to find some users!")
```
## 5_10py:
Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
 - Make a list of five or more usernames called current_users.
 - Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list.
 - Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
 - Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
9 September 2021
"""

current_users = ['user1', 'user2', 'admin', 'user3', 'user4']
new_users = ['1user', '2user', '3user', '4user', '5user']

current_users_lower = [user.lower() for user in current_users] #coded in one line

for new_user in new_users:
  if new_user.lower() in current_users_lower:
     print("Sorry ", new_user, ", that name is taken.")
  else:
     print("Great, ", new_user, " is still available.")
```
## 5_11.py:
Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
 - Store the numbers 1 through 9 in a list.
 - Loop through the list.
 - Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
9 September 2021
"""

numbers = list(range(1,10))
for num in numbers:
  if num == 1:
    print("1st")
  elif num == 2:
    print("2nd")
  elif num == 3:
    print("3rd")
  else:
    print(str(num) + "th")
```
## 5_12.py:
List comprehension which is product of two iterables: initialize a list using a list comprehension which is the product of two iterables that describes students.  Students are either male or female, and a residents of Orange County, LA County or Riverside county.  Print the list.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
9 September 2021
"""
combined = []
for gender in ['Male', 'Female']:
  for county in ['Orange County', 'LA County', 'Riverside County']:
    if gender != county:
      combined.append((gender, county))
print(combined)
```
# Chapter 6: Dictionaries
## 6_1.py:
Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021
"""

person = {
  'first_name': 'Roberto',
  'last_name': 'Suarez',
  'age': 43,
  'city': 'orange',
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])
```
## 6_2.py:
Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. 
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021
"""

favorite_numbers = {
  'Aliyah': 0,
  'Twon': 10,
  'Gary': 9,
  'Henry': 8,
  'Christina': 2,
}

num = favorite_numbers['Aliyah']
print("Aliyah's favorite number is " , str(num) , ".")

num = favorite_numbers['Twon']
print("Twon's favorite number is " , str(num) , ".")

num = favorite_numbers['Gary']
print("Gary's favorite number is " , str(num) , ".")

num = favorite_numbers['Henry']
print("Henry's favorite number is " , str(num) , ".")

num = favorite_numbers['Christina']
print("Christina's favorite number is " , str(num) , ".")
```
## 6_3.py:
Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
 - Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
 - Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.  Use \ to include long definitions.  Use a key, value loop to print the glossary.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021
"""

glossary = {
  'string': 'A series of characters.',
  'comment': 'A note in a program that the Python interpreter ignores.',
  'list': 'A collection of items in a particular order.',
  'loop': 'Work through a collection of items, one at a time.',
  'dictionary': "A collection of key-value pairs.",
}

word = 'string'
print("\n", word.title(), ": ", glossary[word])

word = 'comment'
print("\n", word.title(), ": ", glossary[word])

word = 'list'
print("\n", word.title(), ": ", glossary[word])

word = 'loop'
print("\n", word.title(), ": ", glossary[word])

word = 'dictionary'
print("\n", word.title(),": ", glossary[word])
```
## 6_5.py:
Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
 - Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
 - Use a loop to print the name of each river included in the dictionary.
 - Use a loop to print the name of each country included in the dictionary.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021
"""

rivers = {
    'Nile': 'Egypt',
    'Thames': 'England',
    'Ness': 'Scotland',
    'Blackwater': 'Ireland',
    'Tama': 'Japan',
    }

for river, country in rivers.items():
    print("The ", river.title(), " flows through ", country.title(), ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- ", river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- ", country.title())
```
## 6_6.py:
Polling: Use the code in favorite_languages.py.

Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021
"""

favourite_languages = {
  'Henry': 'Python',
  'James': 'C',
  'Isabelle': 'Ruby',
  'Jack': 'Python',
}

for name, language in favourite_languages.items():
  print(name.title(), "'s favourite language is ", language.title(), ".")

print("\n")

coders = ['Ian', 'Caleb', 'Jose', 'Ken', 'Sally', 'Aaron', 'Wilhelmina']
for coder in coders:
  if coder in favourite_languages.keys():
    print("Thank you for taking the poll, ", coder.title() , "!")
  else:
    print(coder.title(), ", what's your favourite programming language?")
```
## 6_7.py:
People: Start with the program you wrote for 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.  For example, "Neil Thompson is 66 years old and lives in the city of Orange."
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021
"""
people = []
person = {
  'first_name': 'Henry', 
  'last_name': 'Grubstick', #Forgive me, I must...!
  'age': 47,
  'city': 'Fresno',
}
people.append(person)

person = {
  'first_name': 'Aliyah',
  'last_name': 'Millán',
  'age': 19,
  'city': "'hey that's confidential information'", #kek
}
people.append(person)

person = {
  'first_name': 'Jessie',
  'last_name': 'Switcher',
  'age': 23,
  'city': 'Las Vegas',
}
people.append(person)

for person in people:
  name = person['first_name'].title() + " " + person['last_name'].title()
  age = str(person['age'])
  city = person['city'].title()  
  print(name + ", of " + city, ", is " + age + " years old.")
```
## 6_10.py:
Favorite Numbers: Modify your program from 6-2 so each person can have more than one favorite number. For one person, give them three favorite number and for another give them two favorite numbers.  Then print each person’s name along with their favorite numbers.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021
"""

favourite_numbers = {
  'Henry': [42, 17],
  'James': [42, 39, 56],
  'Rob': [7, 12],
}

for name, numbers in favourite_numbers.items():
  print("\n", name.title(), " likes the following numbers:")
  for number in numbers:
    print("  ", str(number))
```
## 6_11.py:
 Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
 ```python
 """
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021
"""
cities = {
 'Mexico City': {
   'country': 'Mexico',
   'population': '8.855 million',
   'fact': "Volcán Popocatépetl, whose name is the Aztec word for smoking mountain, towers to 5426 m 70 km SE of Mexico City to form North America's 2nd-highest volcano. \U0001F30B",
},
  'London': {
    'country': 'England',
    'population': '8.982 million',
    'fact': 'Charles II is the one who ordered 6 ravens to be placed inside the Tower of London in order to protect it. Superstition has continued ever since. \U0001F3F0',
}, #Should I have used the Cleopatra's Needle is a time capsule?
  'Paris': {
        'country': 'France',
        'population': 1003285,
        'fact': "Supposedly, there's only one stop sign in all of Paris. \U0001F6D1",
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']
    
    print("\n" + "\U0001F30E" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print(" One fact about it: " + str(fact))
 ```
 # Chapter 7: User Input and While Loops
## 7_1.py:
Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
22 September 2021
"""

carType = input("What kind of car would you like?\n")
print("Let me see if I can find you a " + carType.title() + "!")
```
## 7_3.py:
Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 September 2021
"""

number = input("Please give me a number: ")
number = int(number)

if number % 10 == 0:
  print(str(number) + " is a multiple of 10.")
else:
  print(str(number) + " isn't a multiple of 10.")
```
## 7_4.py:
Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.
 - Use a conditional test in the while statement to stop the loop.
 - Use an active variable to control how long the loop runs.
When complete, print a formatted message that lists the pizza toppings.
Look at the parrot_flag.py program for an example of an active variable.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 September 2021
"""
prompt = "\nWhat topping would you like on your pizza?"
#+= (operator?) adds another value with the variable's value and assigns the new value to the variable, according to Stack Overflow:
prompt += "\nEnter the word 'done' when you're finished: \n"

while True:
  toppings = input(prompt)
 # != is 'not equal'
  if toppings != 'done': #my conditional statement
    print("I'll add " + toppings + " to your pizza.")
  else:
    break #ends the while loop
```
## 7_5.py:
Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
23 September 2021
"""
prompt = "--> How old are you?"
prompt += "\n--> Enter 'done' when you're finished. \n"
while True:
  age = input(prompt)
  if age == 'done':
    break
  age = int(age)
######################
  if age < 3:
    print("--> You get in free!")
  elif age < 13:
    print("--> Your ticket costs $10.")
  else:
    print("--> Your ticket costs $15.")
```
## 7_8.py:
Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 September 2021
"""
sandwich_order = ['nutella', 'ham and cheese', 'turkey on rye', 'tuna']

completed_sandwich = []

while sandwich_order:
  current_sandwich = sandwich_order.pop()
  print("I'm working on your " + current_sandwich + " sandwich.")
  completed_sandwich.append(current_sandwich)

print("\n")
for sandwich in completed_sandwich:
  print("I made your " + sandwich + " sandwich.")
```
## 7_9.py:
No Pastrami: Using the list sandwich_orders from 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
24 September 2021
"""
sandwich_order = [
    'pastrami', 'ham and cheese', 'Rian-style turkey on rye', 'pastrami',
    'cold ice cream', 'pastrami', 'cheesy, cheesy with cheese']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

print("\n")
while sandwich_order:
    current_sandwich = sandwich_order.pop()
    print("I'm working on your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made you a " + sandwich + " sandwich!")
```
## 7_10.py:
Dream Vacation: Write a program that polls users about their dream vacation. Write a prompt that first asks for the person's name, then asks what country their first dream vacation would be in and then asks what country their second dream vacation would be in. Store the result in a dictionary with the name as the key and the value is a list of destinations. Include a block of code that prints the results of the poll.  See mountain_poll.py
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
25 September 2021

For 7-10 there should be two dream destinations.  One way to add that is to get both destinations, create a small list and then add the list to the dictionary using the key that is the name (of the person).
    """

ask_name = "What's your name? "
ask_place = "If you could visit one place in the world, where would it be? "
ask_continue = "\nWould you like to let someone else leave a response? (yes/no) "
# Keep my responses in the form {name: place}.
responses = {}
while True:
    name = input(ask_name)
    place = input(ask_place)

    # Store response.
    responses[name] = place

    repeat = input(ask_continue)
    if repeat != ('yes'):
        break

print("\n----- Results -----\n")
for name, place in responses.items():
    print(name.title() + " would like to visit " + place.title() + ".")
```
# 7_11.py:
Print Squares and Cubes of X:  Starting with the following code, complete the print statement using .format() such that it produces the attached output:
```python
# Provided Code
print(" x   x**2 x**3")
for x in range(1, 11):
    print(<your code here>)
```
```python
# Provided output

Output:

 x   x**2 x**3
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```
📣 CODE NEEDED 📣

```python
CODE NEEDED
```
## 7_12.py:
**Printing Number:** Create a list containing the following numbers: 123.45, -5.12345, 0.056789.  Print these numbers in this formatted output using an f-string.
```
Number: 123.45

Number: -5.123

Number: 0.05679
```
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
27 September 2021
"""

numList = [round(123.45, 1), round(-5.12345, 3), round(0.056789, 5)]
print(f"Number: {numList[0]}\n\nNumber: {numList[1]}\n\nNumber: {numList[2]}")
```
## 7_13.py:
**More Print Numbers:** Using the list from 7-12, numbers in this formatted output using an str.format(): 
```
Formatted number list:

_______123.45_______

______-5.12345______

______0.056789______
```
```python
""""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
30 September 2021

txt1 = "My name is {fname}, I'm {age}".format(fname = "Jack", age = 27)
txt2 = "My name is {0}, I'm {1}".format("Jack", 27)
txt3 = "My name is {}, I'm {}".format("Jack", 27)

"""
numList = [round(123.45, 1), round(-5.12345, 3), round(0.056789, 5)]
print(f"Number: {numList[0]}\n\nNumber: {numList[1]}\n\nNumber: {numList[2]}")
```
# 7_14.py:
**Table Printing:** Create a list of dictionaries of famous people containing first name, last name, date of birth, birthplace and notable quote.  Print the contents of the dictionary in a formatted table.  Adjust columns to look attractive for your table.  For example:
```
Name                     Birthdate          Birthplace                Quote    

-------------------------------------------------------------------------------------

Ellington, Duke       April 29, 1899  Washington D.C.      Gray skies are just clouds passing over.

Davis, Miles            May 26, 1926    Alton, IL                   I always listen for what I can leave out.

Masamune, Goro   May 26, 1926    Japan                       I made the Honjo Masamune.
```
📣 CODE NEEDED 📣

```python
CODE NEEDED
```
# Chapter 8: Functions and Modules
## 8_1.py:
**Message:** Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
5 October 2021
"""

def display_message():
  message = "I'm learning to code using functions, I think."
  print(message)

display_message()
```
## 8_2.py:
**Favorite Book:** Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
5 October 2021
"""

def favorite_book(book_title):
  print(book_title + " is one of my favorite books.")

favorite_book('The Sound and the Fury')
```
## 8_3.py:
**T-Shirt:** Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
"""

def make_shirt(size, message):
  print("\nI'm going to make a " + size + " t-shirt.")
  print('It will say, "' + message + '"')

make_shirt('small', 'sudo Will you be my Valentine?')
make_shirt(message="I have your IP address. Be afraid.", size='medium')
```
## 8_4.py:
**Large Shirts:** Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
"""

def make_shirt(size='large', message="\nMy name is 'OR1=1;--\nPrepare to die.\n"):

  print("\nI'm going to make a " + size + " t-shirt.")
  print('It will say, "' + message + '"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', "Please stay @ 127.0.0.1. Don't be 255.255.255.255.")
```
## 8_6.py:
**City Names:** Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"

Call your function with at least three city-country pairs, and print the values that are returned.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
"""

def city_country(city, country):
  return(city.title() + ", " + country.title())

city = city_country('paris', 'france')
print(city)

city = city_country('chihuahua', 'mexico')
print(city)

city = city_country('moscow', 'russia')
print(city)
```
## 8_7.py:
**Album:** Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
```python
"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
"""
#Of course I take every opportunity to rep my man Alec
#I made everything with proper capitalisation already out of respect for my man Alec.

def make_album(artist, title, tracks=0):
    album_dictionary = {
        'Artist': artist.title(),
        'Title': title.title(),
        }
    if tracks:
        album_dictionary['Tracks'] = tracks
    return album_dictionary

album = make_album('Alec Benjamin', "Together We'll Fall")
print(album)

album = make_album('Alec Benjamin', 'Older', tracks=4)
print(album)

album = make_album('Alec Benjamin', 'Medicine Man', tracks=0)
print(album)

album = make_album('Alec Benjamin', 'Anesthesia', tracks=2)
print(album)

"""
def make_album(artist, title):
    album_dictionary = {
        'Artist': artist.title(),
        'Title': title.title(),
        }
    return album_dictionary

album = make_album('Alec Benjamin', "Together We'll Fall") #dunno why the first L in ' we'll ' ends up capitalised.... very odd. When I delete the first L, it happens to the second L.
print(album)

album = make_album('Alec Benjamin', 'Older')
print(album)

album = make_album('Alec Benjamin', 'Medicine Man')
print(album)
"""
```





