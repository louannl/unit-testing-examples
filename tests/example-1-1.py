from unittest import TestCase, main
from examples.example_1 import is_string_long

"""
coverage run -m unittest tests/example-1-1.py 
75% coverage
"""

class TestIsStringLong(TestCase):

    def test_returns_false(self):
        result = is_string_long("abc")
        self.assertEqual(result, False)


if __name__ == '__main__':
    main()
