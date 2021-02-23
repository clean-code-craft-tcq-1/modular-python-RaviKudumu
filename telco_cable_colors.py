import telco_cable_pairs_utility
if __name__ == '__main__':
    pair_number = 1
    for major_color in telco_cable_pairs_utility.major_colors:
        for minor_color in telco_cable_pairs_utility.minor_colors:
            print(telco_cable_pairs_utility.telco_cable_pair(major_color, minor_color, pair_number))
            pair_number += 1
