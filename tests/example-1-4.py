from unittest import TestCase, main
from examples.example_4 import is_string_long

"""
 coverage run -m --branch unittest tests/example-1-4.py
 100% Branch and line coverage - with no assertions made
"""


class TestIsStringLong(TestCase):

    def test_absolutely_nothing(self):
        result_1 = is_string_long("abc")
        result_2 = is_string_long("abcdef")


if __name__ == '__main__':
    main()
