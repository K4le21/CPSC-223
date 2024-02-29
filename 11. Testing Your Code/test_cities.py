import unittest
from city_functions import cityCountry

class testMethod(unittest.TestCase):
    def test_city_country(self):
        cityCountry("Santiago", "Chile", 500000)



if __name__ == '__main__':
    unittest.main()