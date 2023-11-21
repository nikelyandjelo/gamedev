from unittest import TestCase
from yahtzee import update_scoresheet_nums


class Test(TestCase):

    def test_update_scoresheet_nums_ones(self):
        expected = 1
        actual = update_scoresheet_nums("One's", [1, 3, 4, 5, 6])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_twos(self):
        expected = 6
        actual = update_scoresheet_nums("One's", [2, 2, 4, 2, 6])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_threes(self):
        expected = 6
        actual = update_scoresheet_nums("Three's", [2, 2, 3, 3, 6])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_fours(self):
        expected = 4
        actual = update_scoresheet_nums("One's", [2, 2, 4, 2, 6])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_fives(self):
        expected = 25
        actual = update_scoresheet_nums("Five's", [5, 5, 5, 5, 5])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_sixes(self):
        expected = 15
        actual = update_scoresheet_nums("Five's", [5, 5, 6, 6, 5])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_no_match(self):
        expected = 0
        actual = update_scoresheet_nums("One's", [5, 5, 6, 6, 5])
        self.assertEqual(expected, actual)
