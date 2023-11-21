from unittest import TestCase
from yahtzee import  update_scoresheet_combo

class Test(TestCase):

    def test_update_scoresheet_nums_three_of_a_kind(self):
        expected = 11
        actual = update_scoresheet_combo("Three of a Kind", [1, 1, 1, 4, 4])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_four_of_a_kind(self):
        expected = 8
        actual = update_scoresheet_combo("Four of a Kind", [1, 1, 1, 1, 4])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_full_house(self):
        expected = 25
        actual = update_scoresheet_combo("Full House", [1, 1, 1, 4, 4])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_small_straight(self):
        expected = 30
        actual = update_scoresheet_combo("Small Straight", [1, 2, 3, 6, 4])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_large_straight(self):
        expected = 40
        actual = update_scoresheet_combo("Large Straight", [1, 2, 3, 5, 4])
        self.assertEqual(expected, actual)

    def test_update_scoresheet_nums_no_match(self):
        expected = 0
        actual = update_scoresheet_combo("Small Straight", [1, 2, 6, 5, 4])
        self.assertEqual(expected, actual)