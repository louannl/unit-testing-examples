from unittest import TestCase

"""
Listing 1.2
----------------------------------
Function lines: 2
Lines executed in test: 2
Test coverage: 2/2 = 100%
----------------------------------
coverage run -m unittest example-1-2.py
coverage report -m
"""


def is_string_long(input: str) -> bool:
    return len(input) > 5


class TestIsStringLong(TestCase):

    def test_returns_false(self):
        result = is_string_long("abc")
        self.assertEqual(result, False)
