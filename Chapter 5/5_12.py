"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
9 September 2021


Instructions:
List comprehension which is product of two iterables: initialize a list using a list comprehension which is the product of two iterables that describes students.  Students are either male or female, and a residents of Orange County, LA County or Riverside county.  Print the list.

"""
combined = []
for gender in ['Male', 'Female']:
  for county in ['Orange County', 'LA County', 'Riverside County']:
    if gender != county:
      combined.append((gender, county))
print(combined)
