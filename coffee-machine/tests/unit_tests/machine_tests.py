import unittest

from coffee_machine import CoffeeMachine


class TestStates(unittest.TestCase):

    def setUp(self):
        self.vending_machine = CoffeeMachine()

    def test_if_coffee_machine_has_correct_initial_state(self):
        self.assertEqual(str(self.vending_machine.state), 'SelectionState')

    def test_if_coffee_machine_change_state_correctly(self):
        self.vending_machine.transition('coffee_picked')
        self.assertEqual(str(self.vending_machine.state), 'PreparingState')

    def test_if_machine_does_not_allow_to_change_state_incorrectly(self):
        with self.assertRaises(RuntimeError):
            self.vending_machine.brewing('asd', 'xxl')

    def test_if_resources_are_correctly_depleted(self):
        self.vending_machine.resource_change(water=10, milk=20)

        self.assertEqual({'water': 90, 'milk': 80}, self.vending_machine.resources)

    def test_if_coffee_brews_correctly(self):
        self.vending_machine.transition('coffee_picked')
        self.assertEqual(str(self.vending_machine.brewing('machiatto', 'xxl')), 'machiatto xxl')


if __name__ == '__main__':

    unittest.main()
