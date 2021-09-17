"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021

"""

rivers = {
    'Nile': 'Egypt',
    'Thames': 'England',
    'Ness': 'Scotland',
    'Blackwater': 'Ireland',
    'Tama': 'Japan',
    }

for river, country in rivers.items():
    print("The ", river.title(), " flows through ", country.title(), ".")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print("- ", river.title())

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print("- ", country.title())
