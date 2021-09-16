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
