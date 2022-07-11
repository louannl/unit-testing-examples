from unittest import TestCase

"""
coverage run -m unittest example-1-3.py
coverage report -m
100%
"""

was_last_string_long = False


def is_string_long(input: str) -> bool:
    result = len(input) > 5
    was_last_string_long = result   # First outcome
    return result   # Second outcome


class TestIsStringLong(TestCase):

    def test_returns_false(self):
        result = is_string_long("abc")
        # Test only verifies the return result line
        self.assertEqual(result, False)
