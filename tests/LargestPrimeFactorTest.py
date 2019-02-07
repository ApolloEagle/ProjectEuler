import unittest

from LargestPrimeFactor import largestPrimeFactor

class TestPrimeFactor(unittest.TestCase):
    def test_num(self):
        num = 600851475143
        result = largestPrimeFactor(num)
        self.assertEqual(result, 6857)

    def test_invalid_type(self):
        num = 'boom'
        with self.assertRaises(TypeError):
            result = largestPrimeFactor(num)

if __name__ == '__main__':
    unittest.main()