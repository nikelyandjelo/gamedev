from unittest import TestCase
from yahtzee import print_hand
import io
from unittest.mock import patch


class Test(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hand_ordered(self, mock_stdout):
        print_hand([1, 2, 3, 4, 5])
        expected = "\n---------------------------------------------------\n" \
                   "---   Your current hand is:\t1\t2\t3\t4\t5\t---\n" \
                   "---------------------------------------------------\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hand_yahtzee(self, mock_stdout):
        print_hand([1, 1, 1, 1, 1])
        expected = "\n-----------------------------------------------------------------\n" \
                   "---   Your current hand is:\t1\t1\t1\t1\t1\tYAHTZEE! ◉_◉ ---" \
                   "\n-----------------------------------------------------------------\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hand_unordered(self, mock_stdout):
        print_hand([4, 2, 3, 1, 4])
        expected = "\n---------------------------------------------------\n" \
                   "---   Your current hand is:\t4\t2\t3\t1\t4\t---\n" \
                   "---------------------------------------------------\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())


