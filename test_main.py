import unittest
from parameterized import parameterized

from main import min_of_three_vars, make_capital_letters, division_by_twelve


class MinOfThreeVarsTestCase(unittest.TestCase):

    @parameterized.expand([
        ("negative", (1, 2, 3), 1),
        ("integer", (2, 1, 3), 1),
        ("large fraction", (3, 2, 1), 1),
    ])
    def test_min_a(self, name, input, expected):
        self.assertEqual(min_of_three_vars(*input), expected)


class TestingEchoFunction(unittest.TestCase):

    @parameterized.expand([
        ("lower", "test", "TEST"),
        ("lower and higher", "hello WORLD", "HELLO WORLD"),
        ("Capital", "Lorem ipsum", "LOREM IPSUM"),
        ("characters", "tests are a cool thing!", "TESTS ARE A COOL THING!"),
    ])
    def test_min_of_three_vars(self, name, input, expected):
        self.assertEqual(make_capital_letters(input), expected)


class TestingDivisionFunction(unittest.TestCase):
    def test_division_by_twelve(self):
        self.assertEqual(division_by_twelve(12), True)
        self.assertEqual(division_by_twelve(13), False)
        self.assertEqual(division_by_twelve("12"), True)
        self.assertEqual(division_by_twelve("Bad Test"), False)
