import unittest

from cats_bats_spiders_beckyw5 import CatsBatsSpiders


class TestCatsBatsSpiders(unittest.TestCase, CatsBatsSpiders):
    def test_cats(self):
        """
        Test that if a number is divisible by 3 it is a Cat
        """
        number = 9
        result = self.cats_bats_spiders_checker(number)
        self.assertEqual(result, 'cats')

    def test_spiders(self):
        """
        Test that if a number is divisible by 3 it is a Cat
        """
        number = 30
        result = self.cats_bats_spiders_checker(number)
        self.assertEqual(result, 'spiders')

    def test_bats(self):
        """
        Test that if a number is divisible by 3 it is a Cat
        """
        number = 10
        result = self.cats_bats_spiders_checker(number)
        self.assertEqual(result, 'bats')


if __name__ == '__main__':
    unittest.main()