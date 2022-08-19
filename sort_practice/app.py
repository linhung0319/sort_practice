import os
import sys

script_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(script_dir, '../'))

from sort_practice.sort_function import *

def main():
    nums = [5, -1, 4, 2, 2]
    #nums = [-1, 0, 1, -1, 5]
    #bubble_sort(nums)
    #selection_sort(nums)
    #insertion_sort(nums)
    #merge_sort(nums)
    #quick_sort(nums)
    heap_sort(nums)
    print(nums)

if __name__ == '__main__':
    main()