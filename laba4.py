import unittest
import math
from rectangle import area_rectangle , perimeter_rectangle
from triangle import area_triangle, perimeter_triangle
from square import area_square, perimeter_square


class TestSquare(unittest.TestCase) :
    def test_square_area(self) :
        self.assertEqual(area_square(1),1)
        self.assertEqual(area_square(4),16)
        self.assertEqual(area_square(5),25)
        self.assertEqual(area_square(0),0)

    def test_square_perimetr(self) :
        self.assertEqual(perimeter_square(1),4)
        self.assertEqual(perimeter_square(4),16)
        self.assertEqual(perimeter_square(5),20)
        self.assertEqual(perimeter_square(0),0)

class TestTriangle(unittest.TestCase) :
    def test_triangle_area(self) :
        self.assertEqual(area_triangle(2,4),4)
        self.assertEqual(area_triangle(5,6),15)
        self.assertEqual(area_triangle(0,4),0)
        self.assertEqual(area_triangle(2,0),0)
    def test_triangle_perimetr(self) :
        self.assertEqual(perimeter_triangle(3, 4, 5), 12)  
        self.assertEqual(perimeter_triangle(1, 4, 5), 10)  
        self.assertEqual(perimeter_triangle(1, 1, 1), 3)

class TestingRectangle(unittest.TestCase) :
    def test_reactangle_area(self) :
        self.assertEqual(area_rectangle(4, 5), 20)
        self.assertEqual(area_rectangle(2, 3), 6)
        self.assertEqual(area_rectangle(0, 3), 0)  

    def test_rectangle_perimeter(self):
        self.assertEqual(perimeter_rectangle(4, 5), 18) 
        self.assertEqual(perimeter_rectangle(2, 3), 10)
        self.assertEqual(perimeter_rectangle(0, 3), 6)


if __name__ == "__main__":
    unittest.main()
