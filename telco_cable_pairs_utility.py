major_colors = ['White', 'Red', 'Black', 'Yellow', 'Violet']
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def cable_colors_for_pair_number(pair_number):
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(minor_colors)
    if major_index >= len(major_colors):
        raise Exception('Major index out of range')
    minor_index = zero_based_pair_number % len(minor_colors)
    if minor_index >= len(minor_colors):
        raise Exception('Minor index out of range')
    return major_colors[major_index], minor_colors[minor_index]

def pair_number_of_cable_colors(major_color, minor_color):
    try:
        major_index = major_colors.index(major_color)
    except ValueError:
        raise Exception('Major index out of range')
    try:
        minor_index = minor_colors.index(minor_color)
    except ValueError:
        raise Exception('Minor index out of range')
    return major_index * len(minor_colors) + minor_index + 1

def telco_cable_pair(major_color, minor_color,  pair_number):
    return f'{pair_number} \t {major_color} \t {minor_color}'