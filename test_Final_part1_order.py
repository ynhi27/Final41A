# Y Nhi Tran
# Final part 1
# This program write a test for menu-driven program for De Anza College Food Court.
# test_Final_part1_order.py

import unittest
from Final_part1_order import Order

class TestCalc(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self._orderDict = None

    def setUp(self):
        print("Setup")


    def tearDown(self):
        print("Teardown")

    def test_getInputs(self):
        print("Test 1 running . . .")

        self.assertEqual(self._orderDict, 'De Anza Burger')


if __name__ == "main":
    unittest.main()