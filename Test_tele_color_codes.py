import unittest
import Tele_Colors_Utility

class TeleColorsTest(unittest.TestCase):
    def test_number_to_pair(self):
        major_color, minor_color = Tele_Colors_Utility.get_color_from_pair_number(4)
        self.assertEqual(major_color, "White")
        self.assertEqual(major_color, "Brown")
        major_color, minor_color = Tele_Colors_Utility.get_color_from_pair_number(5)
        self.assertEqual(major_color, "White")
        self.assertEqual(major_color, "Slate")

    def test_pair_to_number(self):
        pair_number = Tele_Colors_Utility.get_pair_number_from_color("Black", "Orange")
        self.assertEqual(pair_number, 12)
        pair_number = Tele_Colors_Utility.get_pair_number_from_color("Violet", "Slate")
        self.assertEqual(pair_number, 25)
        pair_number = Tele_Colors_Utility.get_pair_number_from_color("Red", "Orange")
        self.assertEqual(pair_number, 7)
if __name__ == "__main__":
  unittest.main()
