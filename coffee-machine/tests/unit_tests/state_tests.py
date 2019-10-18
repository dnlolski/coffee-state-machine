import unittest

from state import State


class TestStates(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def test_state_transition_method_throws_exceptions(self):

        with self.assertRaises(NotImplementedError) as context:
            self.state.transition('101')

    def test_state_class_repr_if_in_correct_format(self):

        test_state = "Testing" + str(self.state.__repr__())

        print(test_state)

        self.assertRegex(test_state, r"^([A-Z][a-z]+)+$")


if __name__ == '__main__':

    unittest.main()
