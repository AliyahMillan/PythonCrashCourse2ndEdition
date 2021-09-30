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
    
    
