import unittest
from mult3 import mult3


class TestMulti3(unittest.TestCase):
    """ Contains Unit Tests for Mult"""

    def test_1(self):  # The function names also can be whatever you want
        a_list = (5, 5, 5)
        result = mult3(*a_list)
        self.assertEqual(result, 125)


if __name__ == '__main__':
    unittest.main()
