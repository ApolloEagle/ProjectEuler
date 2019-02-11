import unittest

from PrimeSum import primeSum

class TestPrimeSum(unittest.TestCase):
    def test_num(self):
        num = 2000000
        result = primes(num)
        self.assertEqual(result, 142913828922)

    def test_invalid_type(self):
        num = 'boom'
        with self.assertRaises(TypeError):
            result = primes(num)

if __name__ == '__main__':
    unittest.main()