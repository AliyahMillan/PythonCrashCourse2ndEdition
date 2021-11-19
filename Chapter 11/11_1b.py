"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
28 October 2021

11-1. City, Country: Write a function that accepts two parameters: a city name and a country name. 
The function should return a single string of the form City, Country, such as Santiago, Chile. Store the function in a module called city_functions.py.
Create a file called test_cities.py that tests the function you just wrote (remember that you need to import unittest and the function you want to test). 
Write a method called test_city_country() to verify that calling your function with values such as 'santiago' and 'chile' results in the correct string. 
Run test_cities.py, and make sure test_city_country() passes.

Turn in only the final versions of city_functions.py and test_cities.py.

This is test_cities.py

8_6.py:
####################################
def city_country(city, country):
  return(city.title() + ", " + country.title())

city = city_country('paris', 'france')
print(city)

city = city_country('chihuahua', 'mexico')
print(city)

city = city_country('moscow', 'russia')
print(city)

"""
import unittest
from main import city_country
#from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
  def test_city_country(self):
    chi_mx = city_country('chihuahua', 'mexico')
    self.assertEqual(chi_mx, 'Chihuahua, Mexico')
unittest.main()
