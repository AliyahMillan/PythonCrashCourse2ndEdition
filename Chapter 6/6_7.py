"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021

"""
people = []
person = {
  'first_name': 'Henry', 
  'last_name': 'Grubstick', #Forgive me, I must...!
  'age': 47,
  'city': 'Fresno',
}
people.append(person)

person = {
  'first_name': 'Aliyah',
  'last_name': 'Millán',
  'age': 19,
  'city': "'hey that's confidential information'", #kek
}
people.append(person)

person = {
  'first_name': 'Jessie',
  'last_name': 'Switcher',
  'age': 23,
  'city': 'Las Vegas',
}
people.append(person)

for person in people:
  name = person['first_name'].title() + " " + person['last_name'].title()
  age = str(person['age'])
  city = person['city'].title()  
  print(name + ", of " + city, ", is " + age + " years old.")
