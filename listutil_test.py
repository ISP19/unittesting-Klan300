import unittest
from listutil import unique

# test by : python3 -m unittest math_test.py
class UniqueTest( unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual([],unique([]))
    
    def test_one_item(self):
        self.assertEqual([5],unique([5]))
        self.assertEqual(["5"],unique(["5"]))
    
    def test_one_item_many_times(self):
        self.assertEqual([5],unique([5,5,5,5,5,5]))
        self.assertEqual(["5"],unique(["5","5","5","5"]))

    def test_two_item(self):
        self.assertEqual([2,4],unique([2,4,4,4,2,4,2,2,2,4]))
        self.assertEqual(["a","A"],unique(["a","a","A","A","A","A","a","a","A"]))
        
    def test_many_item(self):
        self.assertEqual([2,3,4,5],unique([2,2,2,3,3,3,2,3,4,4,5,5,5,4]))
        self.assertEqual(["b","a","A","B"],unique(["b","a","A","b","A","B","b","a","A"]))
        self.assertEqual([2,"2",3,"3",4,"4"],unique([2,2,"2",3,"3","3",4,"4",3,3,4,4,"4","3","2",2,2,4]))

    def test_not_list(self):
        with self.assertRaises(ValueError):
            unique(1)
        with self.assertRaises(ValueError):
            unique("0")
        

if __name__ == "__main__":
    unittest.main('listutil_test')