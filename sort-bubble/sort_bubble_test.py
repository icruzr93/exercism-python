import unittest

from sort_bubble import sort_bubble


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0

class SortBubbleTest(unittest.TestCase):

    def test_main(self):
      self.assertEqual(
        sort_bubble([1,4,2,8,345,123,43,32,5643,63,123,43,2,55,1,234,92]),
        [1,1,2,2,4,8,32,43,43,55,63,92,123,123,234,345,5643]
      )
    
    def test_main2(self):
      self.assertEqual(
        sort_bubble([54,26,93,17,77,31,44,55,20]),
        [17, 20, 26, 31, 44, 54, 55, 77, 93]
      )