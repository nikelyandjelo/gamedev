from unittest import TestCase
from unittest.mock import patch
import io
from yahtzee import POSSIBLE_COMBOS
from yahtzee import update_scoresheet


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["One's"])
    def test_update_scoresheet_general(self, mock_input, mock_stdout):
        update_scoresheet({"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                            "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
                            "Large Straight": None, "Chance": None, "Yahtzee": None}, [1, 1, 3, 3, 5])
        expected = {"One's": 2, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
                    "Large Straight": None, "Chance": None, "Yahtzee": None}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": None}, [1, 1, 3, 3, 5])
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:' \
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> \n'
        self.assertEqual(actual, expected)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["One's"])
    def test_update_scoresheet_nothing_added(self, mock_input, mock_stdout):
        expected = {"One's": 0, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
                    "Large Straight": None, "Chance": None, "Yahtzee": None}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": None}, [3, 6, 4, 3, 5])
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:' \
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> '
        self.assertEqual(actual, expected)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Yahtzee"])
    def test_update_scoresheet_first_yahtzee(self, mock_input, mock_stdout):
        expected = {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
                    "Large Straight": None, "Chance": None, "Yahtzee": 50}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": None}, [6, 6, 6, 6, 6])
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:' \
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> \n'
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Yahtzee"])
    def test_update_scoresheet_second_yahtzee(self, mock_input, mock_stdout):
        expected = {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
                    "Large Straight": None, "Chance": None, "Yahtzee": 100}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": 50}, [6, 6, 6, 6, 6])
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:' \
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> \n'
        self.assertEqual(actual, expected)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Yahtzee"])
    def test_update_scoresheet_nth_yahtzee(self, mock_input, mock_stdout):
        expected = {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
                    "Large Straight": None, "Chance": None, "Yahtzee": 250}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": 200}, [6, 6, 6, 6, 6])
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:' \
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> \n'
        self.assertEqual(actual, expected)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Three of a Kind"])
    def test_update_scoresheet_three_of_a_kind(self, mock_input, mock_stdout):
        expected = {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": 20, "Four of a Kind": None, "Full House": None, "Small Straight": None,
                    "Large Straight": None, "Chance": None, "Yahtzee": None}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": None}, [6, 6, 6, 1, 1])
        self.assertEqual(actual, expected)
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:' \
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> \n'
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Four of a Kind"])
    def test_update_scoresheet_four_of_a_kind(self, mock_input, mock_stdout):
        expected = {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": None, "Four of a Kind": 25, "Full House": None, "Small Straight": None,
                    "Large Straight": None, "Chance": None, "Yahtzee": None}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": None}, [6, 6, 6, 6, 1])
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:' \
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> \n'
        self.assertEqual(actual, expected)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Full House"])
    def test_update_scoresheet_full_house(self, mock_input, mock_stdout):
        expected = {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": None, "Four of a Kind": None, "Full House": 25, "Small Straight": None,
                    "Large Straight": None, "Chance": None, "Yahtzee": None}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": None}, [6, 6, 6, 2, 2])
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:' \
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> \n'
        self.assertEqual(actual, expected)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Small Straight"])
    def test_update_scoresheet_full_house(self, mock_input, mock_stdout):
        expected = {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": 30,
                    "Large Straight": None, "Chance": None, "Yahtzee": None}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": None}, [1, 2, 3, 4, 2])
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:'\
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> \n'
        self.assertEqual(actual, expected)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Large Straight"])
    def test_update_scoresheet_large_straight(self, mock_input, mock_stdout):
        expected = {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
                    "Large Straight": 40, "Chance": None, "Yahtzee": None}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": None}, [1, 2, 3, 4, 5])
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:'\
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> \n'
        self.assertEqual(actual, expected)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["Chance"])
    def test_update_scoresheet_chance(self, mock_input, mock_stdout):
        expected = {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
                    "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
                    "Large Straight": None, "Chance": 15, "Yahtzee": None}
        actual = update_scoresheet(
            {"One's": None, "Two's": None, "Three's": None, "Four's": None, "Five's": None, "Six's": None,
             "Three of a Kind": None, "Four of a Kind": None, "Full House": None, "Small Straight": None,
             "Large Straight": None, "Chance": None, "Yahtzee": None}, [1, 2, 3, 4, 5])
        expected_outp = f'Please enter where you would like to deposit your hand of dice\n Available options:' \
                        f' {str(POSSIBLE_COMBOS()).replace("[", "").replace("]", "")} >>> \n'
        self.assertEqual(actual, expected)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

