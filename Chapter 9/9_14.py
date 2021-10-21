"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
13 October 2021

Lottery: Using the list called series, write a 
function:
  get_get_winning_ticket_number that randomly select[s] 4 numbers and 4 letters from the list.  
Create a 
list called 
  get_winning_ticket_number_list which contains 10 winning ticket numbers. Print this list.
series = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D"]
------------------------------------------------------------------
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


#This honestly looks terrible; need to figure out how to make this code look and work better.
