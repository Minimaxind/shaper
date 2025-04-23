import unittest

from .circle import Circle

class TestCircles(unittest.TestCase):
    def test_area(self):
        a = Circle(1.0).get_area()
        self.assertEqual(round(a, 2), 3.14)

        a = Circle(5.0).get_area()
        self.assertEqual(round(a, 2), 78.54)

    def test_diameter(self):
        for r in (0.1, 1.0, 3.33, 1000.0):
            c = Circle(r)
            self.assertEqual(c.get_diameter(), r*2)

    def test_circumference(self):
        cf = Circle(1.0).get_circumference()
        self.assertEqual(round(cf, 2), 6.28)

        cf = Circle(5.0).get_circumference()
        self.assertEqual(round(cf, 2), 31.42)

if __name__ == "__main__":
    unittest.main()

