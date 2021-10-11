"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
User Profile: Start with a copy of user_profile.py. Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
"""

def build_profile(first, last, **user_info):
    user_info['First_name'] = first
    user_info['Last_name'] = last
    return user_info
    
    
user_profile = build_profile('Aliyah', 'Millán', Location='England',
Field='Computer science')
my_profile = build_profile('Harry', 'Potter', Location = 'Australia', Field = 'Magic')
print(user_profile)
print(my_profile)
