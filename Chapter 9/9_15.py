"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
13 October 2021

Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Starting with your program in 9-14, write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.  Also print the winning ticket number so you can confirm it is on the winning ticket list.  You may want to reduce the number of digits in your winning ticket for test purposes.

Your output may look something like this:

winning ticket list: ['2114AZAD', '8621ZDDA', '53310AABA', '11032DABD', '21071ADAZ', '6184AZZB', '10469DZDZ', '7436ZDBD', '10657DDDZ', '4944DDDA']

number_of_tries to win: 315416

possible winner:  7436ZDBD
--------------------------
"""
from random import choice
series = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D']
num = []
print("Let's see what the winning ticket is...")
get_winning_ticket_number_list = []
while len(get_winning_ticket_number_list) < 10:
  while len(get_winning_ticket_number_list) < 10:
    pulled_item = choice(series)
    if pulled_item not in get_winning_ticket_number_list:
      print(f"  We pulled a {pulled_item}!")
      get_winning_ticket_number_list.append(pulled_item)
      num.append(get_winning_ticket_number_list)
          
print("\nWinning ticket list: ", num)
def check_ticket(played_ticket, winning_ticket_number_list):
    for element in played_ticket:
      if element not in winning_ticket_number_list:
        return False
    return True
def make_random_ticket(chosen):
  ticket = []
  while len(ticket) < 4:
    pulled_item = choice(chosen)
    if pulled_item not in ticket:
      ticket.append(pulled_item)
  return ticket
chosen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D']
get_winning_ticket_number = get_winning_ticket_number_list(chosen)
plays = 0
won = False
max_tries = 1000000
while not won:
  new_ticket = make_random_ticket(chosen)
  won = check_ticket(new_ticket, get_winning_ticket_number)
  plays += 1
  if plays >= max_tries:
      break
if won:
  print("There's a winning ticket!")
  print(f"Your ticket reads: {new_ticket}")
  print(f"The winning ticket reads: {get_winning_ticket_number}")
  print(f"{plays} times' the charm!")
else:
  print(f"Tried {plays} times, without pulling a winner. How sad.")
  print(f"Your ticket reads: {new_ticket}")
  print(f"The winning ticket reads: {get_winning_ticket_number_list}")
  
  
#This could also use improvements, coding-wise
