import unittest
from sort_practice.sort_function import bubble_sort

class Test_sort_function(unittest.TestCase):
    def setUp(self):
        self.q1 = [1, 5, -2, 4, 7, 0]
        self.q1_ascend_ans = [-2, 0, 1, 4, 5, 7]

        self.q2 = [1, -1, 0, 0, 3, 2, 3]
        self.q2_ascend_ans = [-1, 0, 0, 1, 2, 3, 3]
    
        self.q3 = [0, 0, 0, 0, 0, 0]
        self.q3_ascend_ans = [0, 0, 0, 0, 0, 0]
       
        self.q4 = [-5, -8, 2, 7, 0, 3, 0, -5]
        self.q4_descend_ans = [7, 3, 2, 0, 0, -5, -5, -8]
    
    def test_bubble_sort(self):
        bubble_sort(self.q1)
        self.assertEqual(self.q1, self.q1_ascend_ans)
        
        bubble_sort(self.q2)
        self.assertEqual(self.q2, self.q2_ascend_ans)
        
        bubble_sort(self.q3)
        self.assertEqual(self.q3, self.q3_ascend_ans)
        
        bubble_sort(self.q4, reverse=True)
        self.assertEqual(self.q4, self.q4_descend_ans)

    