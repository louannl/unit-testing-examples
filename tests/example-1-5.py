from unittest import TestCase
from examples.example_5 import some_parsing_thing


class TestIsStringLong(TestCase):

    def test_that_parser(self):
        result = some_parsing_thing("5")
        self.assertEqual(5, result)

