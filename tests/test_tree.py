
import unittest
from sort_practice.tree import *

class Test_Heap(unittest.TestCase):
    def test_min_heap_push(self):
        min_heap = Heap()
        min_heap.push(1)
        self.assertEqual(min_heap.show(), [1])
        
        min_heap.push(-1)
        self.assertEqual(min_heap.show(), [-1, 1])
        
        min_heap.push(2)
        self.assertEqual(min_heap.show(), [-1, 1, 2])
        
        min_heap.push(-1)
        self.assertEqual(min_heap.show(), [-1, -1, 2, 1])

    def test_max_heap_push(self):
        max_heap = Heap(reverse=True)
        max_heap.push(1)
        self.assertEqual(max_heap.show(), [1])

        max_heap.push(-1)
        self.assertEqual(max_heap.show(), [1, -1])

        max_heap.push(2)
        self.assertEqual(max_heap.show(), [2, -1, 1])

        max_heap.push(2)
        self.assertEqual(max_heap.show(), [2, 2, 1, -1])

