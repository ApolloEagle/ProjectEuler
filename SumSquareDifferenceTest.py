import unittest

from SumSquareDifference import sumSquareDifference

class TestSumSquareDifference(unittest.TestCase):
    def test_num(self):
        num = 100
        result = sumSquareDifference(num)
        self.assertEqual(result, 25164150)

    def test_invalid_type(self):
        num = 'boom'
        with self.assertRaises(TypeError):
            result = sumSquareDifference(num)

if __name__ == '__main__':
    unittest.main()