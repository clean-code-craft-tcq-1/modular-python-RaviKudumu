import unittest
import telco_cable_pairs_utility

class TeleColorsTest(unittest.TestCase):
    def test_number_to_pair(self):
        major_color, minor_color = telco_cable_pairs_utility.cable_colors_for_pair_number(4)
        self.assertEqual(major_color, "White")
        self.assertEqual(minor_color, "Brown")
        major_color, minor_color = telco_cable_pairs_utility.cable_colors_for_pair_number(5)
        self.assertEqual(major_color, "White")
        self.assertEqual(minor_color, "Slate")

    def test_pair_to_number(self):
        pair_number = telco_cable_pairs_utility.pair_number_of_cable_colors("Black", "Orange")
        self.assertEqual(pair_number, 12)
        pair_number = telco_cable_pairs_utility.pair_number_of_cable_colors("Violet", "Slate")
        self.assertEqual(pair_number, 25)
        pair_number = telco_cable_pairs_utility.pair_number_of_cable_colors("Red", "Orange")
        self.assertEqual(pair_number, 7)
if __name__ == "__main__":
  unittest.main()
