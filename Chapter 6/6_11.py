"""
Aliyah Alexis Millán
CPSC-223P Section 1/Section 2
16 September 2021

Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.

"""
cities = {
 'Mexico City': {
   'country': 'Mexico',
   'population': '8.855 million',
   'fact': "Volcán Popocatépetl, whose name is the Aztec word for smoking mountain, towers to 5426 m 70 km SE of Mexico City to form North America's 2nd-highest volcano. \U0001F30B",
},
  'London': {
    'country': 'England',
    'population': '8.982 million',
    'fact': 'Charles II is the one who ordered 6 ravens to be placed inside the Tower of London in order to protect it. Superstition has continued ever since. \U0001F3F0',
}, #Should I have used the Cleopatra's Needle is a time capsule?
  'Paris': {
        'country': 'France',
        'population': 1003285,
        'fact': "Supposedly, there's only one stop sign in all of Paris. \U0001F6D1",
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']
    
    print("\n" + "\U0001F30E" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print(" One fact about it: " + str(fact))
