from unittest import TestCase
from yahtzee import check_list

class Test(TestCase):

    def test_check_list(self):
        expected = True
        actual = check_list(['1', '2', '3', '4'])
        self.assertEqual(expected, actual)

    def test_check_list_empty_list(self):
        expected = False
        actual = check_list([])
        self.assertEqual(expected, actual)

    def test_check_list_contains_alphabets(self):
        expected = False
        actual = check_list(['a', '2', '3', '4'])
        self.assertEqual(expected, actual)

    def test_check_list_over_5_dig(self):
        expected = False
        actual = check_list(['1', '2', '3', '4', '5', '6'])
        self.assertEqual(expected, actual)

    def test_check_list_repeating_dig(self):
        expected = False
        actual = check_list(['1', '1', '3', '4'])
        self.assertEqual(expected, actual)

    def test_check_list_single_dig(self):
        expected = True
        actual = check_list(['1'])
        self.assertEqual(expected, actual)

    def test_check_list_five_dig(self):
        expected = True
        actual = check_list(['1', '2', '3', '4', '5'])
        self.assertEqual(expected, actual)

    def test_check_list_invalid_dig(self):
        expected = False
        actual = check_list(['7', '6', '-1'])
        self.assertEqual(expected, actual)

    def test_check_list_invalid_digits2(self):
        expected = False
        actual = check_list(['12', '34'])
        self.assertEqual(expected, actual)

