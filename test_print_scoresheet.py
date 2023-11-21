from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import print_scoresheet


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scoresheet(self, mock_stdout):
        print_scoresheet({"One's": 4, "Two's": 8, "Three's": 12, "Four's": 16, "Five's": 25,
                          "Six's": 36, "Three of a Kind": 0, "Four of a Kind": 0,
                          "Full House": 0, "Small Straight": 0, "Large Straight": 0,
                          "Chance": 0, "Yahtzee": 0})
        expected = "-----------------\nOne's:\t4\nTwo's:\t8\nThree's:\t12\nFour's:\t16\nFive's:\t25\nSix's:\t36" \
                   "\nThree of a Kind:\t0\nFour of a Kind:\t0\nFull House:\t0\nSmall Straight:\t0" \
                   "\nLarge Straight:\t0\nChance:\t0\nYahtzee:\t0\n-----------------\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scoresheet_everything_filled(self, mock_stdout):
        print_scoresheet({"One's": 4, "Two's": 8, "Three's": 12, "Four's": 16, "Five's": 25,
                          "Six's": 36, "Three of a Kind": 8, "Four of a Kind": 5,
                          "Full House": 25, "Small Straight": 30, "Large Straight": 40,
                          "Chance": 18, "Yahtzee": 150})
        expected = "-----------------\nOne's:\t4\nTwo's:\t8\nThree's:\t12\nFour's:\t16\nFive's:\t25\nSix's:\t36" \
                   "\nThree of a Kind:\t8\nFour of a Kind:\t5\nFull House:\t25\nSmall Straight:\t30" \
                   "\nLarge Straight:\t40\nChance:\t18\nYahtzee:\t150\n-----------------\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected)
