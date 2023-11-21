from unittest import TestCase
from yahtzee import update_scoresheet_combo_yahtzee


class Test(TestCase):

    def test_update_scoresheet_combo_yahtzee_first_time(self):
        expected = 50
        actual = update_scoresheet_combo_yahtzee({"One's": 1, "Two's": 8, "Three's": 12, "Four's": 16, "Five's": 25,
                                                   "Six's": 36, "Three of a Kind": 0, "Four of a Kind": 0,
                                                   "Full House": 0, "Small Straight": 0, "Large Straight": 0,
                                                   "Chance": 0, "Yahtzee": None})
        self.assertEqual(expected, actual)

    def test_update_scoresheet_combo_yahtzee_second_time(self):
        expected = 100
        actual = update_scoresheet_combo_yahtzee({"One's": 2, "Two's": 8, "Three's": 12, "Four's": 16, "Five's": 25,
                                                   "Six's": 36, "Three of a Kind": 0, "Four of a Kind": 0,
                                                   "Full House": 0, "Small Straight": 0, "Large Straight": 0,
                                                   "Chance": 0, "Yahtzee": 50})
        self.assertEqual(expected, actual)

    def test_update_scoresheet_combo_yahtzee_nth_time(self):
        expected = 1500
        actual = update_scoresheet_combo_yahtzee({"One's": 3, "Two's": 8, "Three's": 12, "Four's": 16, "Five's": 25,
                                                   "Six's": 36, "Three of a Kind": 0, "Four of a Kind": 0,
                                                   "Full House": 0, "Small Straight": 0, "Large Straight": 0,
                                                   "Chance": 0, "Yahtzee": 1450})
        self.assertEqual(expected, actual)
