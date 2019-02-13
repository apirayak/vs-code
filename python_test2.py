import unittest
from python_test1 import random_face_color
from enum import Enum
from collections import Counter

class ColorEnum(Enum):
    red = 0
    blue = 1
    green = 2
    yellow = 3
    white = 4
    black = 5

class TestRandomFaceColorCubic(unittest.TestCase):

    def test_nine_colors_correct(self):
        input  = {'frontView' : [None for _ in range(9)],
                  'topView' : [None for _ in range(9)],
                  'buttomView' : [None for _ in range(9)],
                  'leftView' : [None for _ in range(9)],
                  'rightView' : [None for _ in range(9)],
                  'backView' : [None for _ in range(9)] }
        remaining_random_color = [9,9,9,9,9,9]
        result = [0,0,0,0,0,0]
        random_face_color(input)
        for key in input:
            for color_code in range(6):
                result[color_code] += input[key].count(ColorEnum(color_code).name)
        self.assertEqual(result,remaining_random_color)

    def test_is_color_usable(self):
        pass

if __name__ == '__main__':
    unittest.main()

