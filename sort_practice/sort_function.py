
### compare if a > b
def compare(a, b, reverse=False):
    if not reverse:
        return a > b
    else:
        return a < b

def bubble_sort(nums, key=lambda x: x, reverse=False):
    disorder = len(nums) - 1
    while disorder > 0:
        ### list is disordered before the index of last_swap
        last_swap = 0
        ### swap the adjacent from index 1 to disorder
        for i in range(1, disorder + 1):
            if compare(key(nums[i-1]), key(nums[i]), reverse=reverse):
                nums[i-1], nums[i] = nums[i], nums[i-1]
                last_swap = i
        disorder = last_swap - 1

def selection_sort(nums, key=lambda x: x, reverse=False):
    n = len(nums)
    for i in range(n):
        ### iterate through the unsorted part of
        ### array to find the minimum value
        min_i, min_v = i, nums[i] 
        for j in range(i + 1, n):
            if compare(key(min_v), key(nums[j]), reverse):
                min_v = nums[j]
                min_i = j
        ### swap the minimum value with the first value of
        ### to place the minimum in front of the unsorted array
        nums[i], nums[min_i] = nums[min_i], nums[i]    
        

if __name__ == '__main__':
    nums = [5, -1, 4, 2, 2]
    #bubble_sort(nums)
    selection_sort(nums)
    print(nums)