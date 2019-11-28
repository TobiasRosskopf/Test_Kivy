#! python3.8
# -*- coding: utf-8 -*-

# File name:    test_kivy_calculator.py
# Author:       Tobias Rosskopf
# Email:        tobirosskopf@gmail.com
# Created:      28.11.2019
# Modified:     28.11.2019

"""
Unittest for module kivy_calculator.py.
"""

# Standard imports
import unittest

# Package imports
import kivy_calculator.kivy_calculator


class TestKivyCalculator(unittest.TestCase):
    """TODO: Testclass's docstring"""

    def test_eval(self):
        """TODO: Test's docstring"""
        query = "34 * 5 / 7"
        solution = "24.285714285714285"
        self.assertEqual(str(eval(query)), solution)


if __name__ == '__main__':
    unittest.main()
