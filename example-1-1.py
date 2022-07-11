from unittest import TestCase

"""
Listing 1.1
----------------------------------
Function lines: 4
Lines executed in test: 3
Test coverage: 3/4 = 75%
"""


def is_string_long(input: str) -> bool:
    if len(input) > 5:
        return True # Line not covered by below test case
    return False


class TestIsStringLong(TestCase):

    def test_returns_false(self):
        result = is_string_long("abc")
        self.assertEqual(result, False)
