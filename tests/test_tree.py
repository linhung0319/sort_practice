
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

    def test_heapify(self):
        min_heap = Heap()
        x = [-1, 7, 6, 5, 4, 7, -1]
        min_heap.heapify(x)
        self.assertEqual(min_heap.show(), [-1, 4, -1, 7, 5, 7, 6])

        max_heap = Heap(reverse=True)
        max_heap.heapify(x)
        self.assertEqual(max_heap.show(), [7, 5, 7, -1, 4, 6, -1])

    def test_pop(self):
        x = [-1, 7, 6, 5, 4, 7, -1]
        min_heap = Heap(x)
        self.assertEqual(min_heap.pop(), -1)
        self.assertEqual(min_heap.pop(), -1)
        self.assertEqual(min_heap.pop(), 4)

        max_heap = Heap(x, reverse=True)
        self.assertEqual(max_heap.pop(), 7)
        self.assertEqual(max_heap.pop(), 7)
        self.assertEqual(max_heap.pop(), 6)