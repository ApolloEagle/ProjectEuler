import unittest

from SmallestMultiple import smallestMultiple

class TestSmallestMultiple(unittest.TestCase):
    def test_num(self):
        num = 20
        result = smallestMultiple(num)
        self.assertEqual(result, 232792560)

    def test_invalid_type(self):
        num = 'boom'
        with self.assertRaises(TypeError):
            result = smallestMultiple(num)

if __name__ == '__main__':
    unittest.main()