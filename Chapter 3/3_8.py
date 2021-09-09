'''
Seeing the World: Think of at least five places in the world you’d like to visit.  For this program, format the output nicely to indicate what the operation is.  Also, include a brief comment in your code to indicate the intent of the operation.

Store the locations in a list. Make sure the list is not in alphabetical order.
Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
Use sorted() to print your list in alphabetical order without modifying the actual list.
Show that your list is still in its original order by printing it.
Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
Show that your list is still in its original order by printing it again.
Use reverse to change the order of your list. Print the list to show that its order has changed.
Reestablish your original list.
Use a combination of remove() and sorted() to remove the alphabetically first occurring value.  In the case of a list of animals, Aardvard is likely to be removed.  Print the list to show that its order has not changed.
Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
'''
#############################################################################################################################################################################
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
