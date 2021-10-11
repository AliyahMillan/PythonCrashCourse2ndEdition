"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
7 October 2021
"""

def city_country(city, country):
  return(city.title() + ", " + country.title())

city = city_country('paris', 'france')
print(city)

city = city_country('chihuahua', 'mexico')
print(city)

city = city_country('moscow', 'russia')
print(city)
