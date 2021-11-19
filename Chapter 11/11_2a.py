"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
28 October 2021

11-2. Population: Modify your function so it requires a third parameter, population. 
It should now return a single string of the form City, Country – population xxx, such as Santiago, Chile – population 5000000. 
Run test_cities.py again. Make sure test_city_country() fails this time.

Modify the function so the population parameter is optional. Run test_cities.py again, and make sure test_city_country() passes again.

Write a second test called test_city_country_population() that verifies you can call your function with the values 'santiago', 'chile', and population=5000000. 
Run test_cities.py again, and make sure this new test passes.

Turn in only the final versions of city_functions.py and test_cities.py.

This is cities.py
"""
def city_country(city, country, population=0):
  output_string = city.title() + ", " + country.title()
  if population:
    output_string += ' - population ' + str(population)
  return output_string
