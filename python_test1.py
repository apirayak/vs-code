import random
from enum import Enum
from collections import Counter

class ColorEnum(Enum):
    red = 0
    blue = 1
    green = 2
    yellow = 3
    white = 4
    black = 5


def display_face_view(face_dict):
    i = 0
    while i < 7:
        print(face_dict[i], face_dict[i + 1], face_dict[i + 2])
        i += 3


def is_color_usable(color_code,color_list):
    #count color
    usable = False
    is_empty_random_slot = all(remain_count == 9 for remain_count in color_list)
    #check every index have 6 colors
    if not is_empty_random_slot:
        remain_count = color_list[color_code]
        if remain_count < 9:
            color_list[color_code] = remain_count + 1
            usable = False
        elif remain_count >= 9:
            usable = True
    return usable


def random_face_color(face_dict):
    remaining_random_color = [0,0,0,0,0,0]
    for key in face_dict:
        for face_position in range(9):
            usable = True
            while usable:
                color_code = random.randint(0, 5)
                usable = is_color_usable(color_code,remaining_random_color)
                if not usable:
                    face_dict[key][face_position] = ColorEnum(color_code).name
    return face_dict

def generate_dic():
    dictionary =  {'frontView' : [None for _ in range(9)],
        'topView' : [None for _ in range(9)],
        'buttomView' : [None for _ in range(9)],
        'leftView' : [None for _ in range(9)],
        'rightView' : [None for _ in range(9)],
        'backView' : [None for _ in range(9)]}
    return dictionary


face_dict = generate_dic()
cubic = random_face_color(face_dict)
print(cubic) 


