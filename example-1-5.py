from unittest import TestCase

"""
coverage run -m unittest example-1-5.py
coverage report -m
"""


def some_parsing_thing(input: str) -> int:
    return int(input)


class TestIsStringLong(TestCase):

    def test_that_parser(self):
        result = some_parsing_thing("5")
        self.assertEqual(5, result)


if __name__ == "__main__":
    some_parsing_thing("invalid_string")
