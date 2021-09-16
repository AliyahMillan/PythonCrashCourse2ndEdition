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
