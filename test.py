import unittest
from util import average

# test by : python3 -m unittest math_test.py
class MathTest( unittest.TestCase):
    def test_single_list(self):
        self.assertEqual(5,average([5]))
        self.assertEqual(0,average([0]))
        
    def test_many_in_list(self):
        self.assertEqual(2.5,average([2 ,4,-4,8]))
    
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            avg = average([])


if __name__ == "__main__":
    unittest.main('test')