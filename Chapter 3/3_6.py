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
###################
