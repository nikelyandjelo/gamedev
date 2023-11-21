from unittest import TestCase
from yahtzee import submit_scoresheet


class Test(TestCase):

    def test_submit_scoresheet(self):
        expected = {"One's": 1, "Two's": 2, "Three's": 3, "Four's": 4, "Five's": 0, "Six's": 0, "Bonus": 0,
                    "Three of a Kind": 0, "Four of a Kind": 0, "Full House": 0, "Small Straight": 0,
                    "Large Straight": 0,
                    "Chance": 0, "Yahtzee": 0, "Total": 10}
        actual = submit_scoresheet({"One's": 1, "Two's": 2, "Three's": 3, "Four's": 4, "Five's": 0,
                                    "Six's": 0, "Three of a Kind": 0, "Four of a Kind": 0,
                                    "Full House": 0, "Small Straight": 0, "Large Straight": 0,
                                    "Chance": 0, "Yahtzee": 0})
        self.assertEqual(expected, actual)

    def test_submit_scoresheet_bonus(self):
        expected = {"One's": 4, "Two's": 8, "Three's": 12, "Four's": 16, "Five's": 25, "Six's": 36, "Bonus": 35,
                    "Three of a Kind": 0, "Four of a Kind": 0, "Full House": 0, "Small Straight": 0,
                    "Large Straight": 0,
                    "Chance": 0, "Yahtzee": 0, "Total": 136}
        actual = submit_scoresheet({"One's": 4, "Two's": 8, "Three's": 12, "Four's": 16, "Five's": 25,
                                    "Six's": 36, "Three of a Kind": 0, "Four of a Kind": 0,
                                    "Full House": 0, "Small Straight": 0, "Large Straight": 0,
                                    "Chance": 0, "Yahtzee": 0})
        self.assertEqual(expected, actual)

    def test_submit_scoresheet_everything_filled(self):
        expected = {"One's": 4, "Two's": 8, "Three's": 12, "Four's": 16, "Five's": 25, "Six's": 36, "Bonus": 35,
                    "Three of a Kind": 5, "Four of a Kind": 6, "Full House": 25, "Small Straight": 30,
                    "Large Straight": 40, "Chance": 15, "Yahtzee": 50, "Total": 199}
        actual = submit_scoresheet({"One's": 4, "Two's": 8, "Three's": 12, "Four's": 16, "Five's": 25, "Six's": 36,
                                    "Three of a Kind": 5, "Four of a Kind": 6, "Full House": 25, "Small Straight": 30,
                                    "Large Straight": 40, "Chance": 15, "Yahtzee": 50})
        self.assertEqual(expected, actual)
