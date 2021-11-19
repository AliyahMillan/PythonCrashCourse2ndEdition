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


This is test_cities.py
"""
import unittest

#from city_functions import city_country
from main import city_country
class CitiesTestCase(unittest.TestCase):
  def test_city_country(self):
    chi_mx = city_country('chihuahua', 'mexico')
    self.assertEqual(chi_mx, 'Chihuahua, Mexico')

    def test_city_country_population(self):
      chi_mx = city_country('chihuahua', 'mexico', population=878000)
      self.assertEqual(chi_mx, 'Chihuahua, Mexico - population 878000')
unittest.main()
