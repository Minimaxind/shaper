import unittest

class TestExamples(unittest.TestCase):

    def test_add(self):
        self.assertEqual(1 + 5, 6)

    def test_subtract(self):
        self.assertEqual(5 - 5, 0)
        self.assertEqual(50 - 20, 30)

class OtherTestExamples(unittest.TestCase):

    def test_round(self):
        self.assertEqual(round(1.333333, 2), 1.33)

