import unittest
import shapes

class TestShapes(unittest.TestCase):

    def test_add(self):
        self.assertEqual(shapes.add(2, 3), 5)
        self.assertEqual(shapes.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(shapes.subtract(10, 5), 5)
        self.assertEqual(shapes.subtract(0, 10), -10)

    def test_multiply(self):
        self.assertEqual(shapes.multiply(3, 4), 12)
        self.assertEqual(shapes.multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(shapes.divide(10, 2), 5)
        self.assertEqual(shapes.divide(9, 3), 3)
        with self.assertRaises(ValueError):
            shapes.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
