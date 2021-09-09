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
