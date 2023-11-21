from unittest import TestCase
from unittest.mock import patch
from yahtzee import roll_dice
import io


class Test(TestCase):

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch("random.randint", return_value=1)
    def test_roll_dice_one_re_roll(self, mock_stdout, mock_input, mock_randint):
        expected = [1, 1, 3, 4, 5]
        expected_outp = '\nEnter the index of dice you would like to re-roll (1-6). The unselected dice will remain ' \
                        'the same>>> \n'
        actual = roll_dice([1, 2, 3, 4, 5])
        self.assertEqual(expected, actual)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch("random.randint", side_effect=[6, 6, 6])
    @patch('builtins.input', side_effect=['2 4 5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_dice_three_re_roll(self, mock_input, mock_randint, mock_stdout):
        expected = [1, 1, 3, 4, 5]
        expected_outp = '\nEnter the index of dice you would like to re-roll (1-6). The unselected dice will remain ' \
                        'the same>>> \n\nThe list of indices you entered is invalid. Valid dice numbers are 1-6'\
                        'Enter the index of dice you would'' like to re-roll.' \
                        ' The unselected dice will remain the same>>> \n'
        actual = roll_dice([1, 6, 3, 6, 6])
        self.assertEqual(expected, actual)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

    @patch("random.randint", side_effect=[6, 6, 6, 6, 6])
    @patch('builtins.input', side_effect=['1 2 3 4 5'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_roll_dice_all_re_roll(self, mock_input, mock_randint, mock_stdout):
        expected = [6, 6, 6, 6, 6]
        expected_outp = '\nEnter the index of dice you would like to re-roll (1-6). The unselected dice will remain ' \
                        'the same>>> \n'
        actual = roll_dice([1, 6, 3, 6, 6])
        self.assertEqual(expected, actual)
        self.assertEqual(expected_outp, mock_stdout.getvalue())

