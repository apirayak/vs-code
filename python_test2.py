import unittest
from python_test1 import random_face_color
from python_test1 import is_color_usable
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
        remaining_random_color = [0,0,0,0,0,0]
        #ตั้งค่าตัวแปรตรงกันข้ามเพื่อเช็คผลลัพธ์
        result_case1 = True
        result_case2 = False
        #ตัวแปรที่ใส่ มีค่าเท่านี้ ผลลัพธ์ต้องเป็น true 
        #case 1 : ถ้าสีที่ใส่ยังไม่ถึง 10 ผลลัพธ์จะต้องเป็น False ทั้งหมด
        #case 2 : ถ้าสีที่ใส่เกิน 9 แล้วผลลัพธ์จะต้องออกเป็น True   
        #for นอกเป็นสี 6 สี
        for x in range(6):
            #ตำแหน่ง 9 ตำแหน่ง
            for y in range(10):
                result_case1 = is_color_usable(x,remaining_random_color)
                if result_case1 == True and y > 9:
                    result_case2 = True
        #ถ้าครบทั้ง 2 ข้อคือใช้งานได้จะต้องออกเป็น true 
        self.assertEqual(result_case1,result_case2)
        #เช็คว่าถ้าให้ color code เท่านี้ๆ มา จะให้ค่า true false ถูกมั้ย
if __name__ == '__main__':
    unittest.main()

