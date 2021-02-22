import unittest
from Tele_Colors_Utility import *
class TeleColorsTest(unittest.TestCase):
    def test_number_to_pair(self):
        major_color, minor_color = Tele_Colors_Utility.get_color_from_pair_number(4)
        self.assertAlmostEqual(major_color, 'White')
        self.assertAlmostEqual(major_color, 'Brown')
        major_color, minor_color = Tele_Colors_Utility.get_color_from_pair_number(5)
        self.assertAlmostEqual(major_color, 'White')
        self.assertAlmostEqual(major_color, 'Slate')
    def test_pair_to_number(self,major_color):
        pair_number = Tele_Colors_Utility.get_pair_number_from_color('Black', 'Orange')
        self.assertAlmostEqual(pair_number, 12)
        pair_number = Tele_Colors_Utility.get_pair_number_from_color('Violet', 'Slate')
        self.assertAlmostEqual(pair_number, 25)
        pair_number = Tele_Colors_Utility.get_pair_number_from_color('Red', 'Orange')
        self.assertAlmostEqual(pair_number, 7)
if __name__ == "__main__":
  unittest.main()
