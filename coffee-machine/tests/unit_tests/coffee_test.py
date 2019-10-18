import unittest

from coffee.coffee import Coffee


class TestCoffeeClass(unittest.TestCase):

    coffee_type = 1
    coffee_size = "2"

    def test_should_coffee_returns_strings(self):
            coffee_type = self.coffee_type
            size = self.coffee_size
            coffee = Coffee(coffee_type, size)
            print(coffee)

            self.assertIsInstance(coffee.coffee_type, str)
            self.assertIsInstance(coffee.size, str)


if __name__ == '__main__':

    unittest.main()
