#!/usr/bin/env python
import unittest
def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        results = add_numbers(2, 3)
        self.assertEqual(results, 6)
    if __name__ == '__main__':
        unittest.main()
