from unittest import TestCase, main
from examples.example_3 import is_string_long

"""
 coverage run -m --branch unittest tests/example-1-3.py
 100% line coverage
 100% branch coverage
"""


class TestIsStringLong(TestCase):

    def test_returns_false(self):
        result = is_string_long("abc")
        # Test only verifies the return result line
        self.assertEqual(result, False)


if __name__ == '__main__':
    main()
