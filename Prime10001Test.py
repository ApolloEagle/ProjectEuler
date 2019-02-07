import unittest

from Prime10001 import primes

class TestPrimes(unittest.TestCase):
    def test_num(self):
        num = 10001
        result = primes(num)
        self.assertEqual(result, 104743)

    def test_invalid_type(self):
        num = 'boom'
        with self.assertRaises(TypeError):
            result = primes(num)

if __name__ == '__main__':
    unittest.main()