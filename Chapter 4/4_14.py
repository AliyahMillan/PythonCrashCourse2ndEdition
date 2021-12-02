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
