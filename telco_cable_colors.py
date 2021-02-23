import telco_cable_pairs_utility
if __name__ == '__main__':
    pair_number = 1
    for major_color in Tele_Colors_Utility.major_colors:
        for minor_color in Tele_Colors_Utility.minor_colors:
            print(Tele_Colors_Utility.telco_cable_pair(major_color, minor_color, pair_number))
            pair_number += 1