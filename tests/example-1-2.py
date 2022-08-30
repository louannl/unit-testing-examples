from unittest import TestCase, main
from examples.example_2 import is_string_long

"""
coverage run -m --branch unittest tests/example-1-2.py 
"""

class TestIsStringLong(TestCase):

    def test_returns_false(self):
        result = is_string_long("abc")
        self.assertEqual(result, False)


if __name__ == '__main__':
    main()
