import unittest

from PythagoreanTriplet import pythagoreanTriplet

class TestPythagoreanTriplet(unittest.TestCase):
    def test_num(self):
        num = 1000
        result = pythagoreanTriplet(num)
        self.assertEqual(result, 31875000)

    def test_invalid_type(self):
        num = 'boom'
        with self.assertRaises(TypeError):
            result = pythagoreanTriplet(num)

if __name__ == '__main__':
    unittest.main()