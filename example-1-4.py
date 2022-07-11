from unittest import TestCase

"""
coverage run -m unittest example-1-4.py
coverage report -m
"""

was_last_string_long = False


def is_string_long(input: str) -> bool:
    result = len(input) > 5
    was_last_string_long = result   # First outcome
    return result   # Second outcome


class TestIsStringLong(TestCase):

    def test_absolutely_nothing(self):
        result_1 = is_string_long("abc")
        result_2 = is_string_long("abcdef")
