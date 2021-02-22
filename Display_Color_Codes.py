from Tele_Colors_Utility import *
def color_pair_to_string(major_color, minor_color,  pair_number):
    return f'{pair_number} \t {major_color} \t {minor_color}'
pair_number = 1
for major_color in Tele_Colors_Utility.major_colors:
    for minor_color in Tele_Colors_Utility.minor_colors:
        print(color_pair_to_string(major_color, minor_color, pair_number))
        pair_number += 1
