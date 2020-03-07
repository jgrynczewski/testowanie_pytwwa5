import unittest
import math

import cir_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        """Test area when radius >= 0"""
        self.assertAlmostEqual(cir_area.circle_area(1), math.pi)
        self.assertAlmostEqual(cir_area.circle_area(0), 0)
        self.assertAlmostEqual(cir_area.circle_area(2.1), 13.85, 2)

    def test_values(self):
        self.assertRaises(ValueError, cir_area.circle_area, -1)

    def test_types(self):
        """Make sure type error is raise when necessary"""
        self.assertRaises(TypeError, cir_area.circle_area, 3+5j)
        self.assertRaises(TypeError, cir_area.circle_area, "radius")
        self.assertRaises(TypeError, cir_area.circle_area, False)

if __name__=="__main__":
    unittest.main()
