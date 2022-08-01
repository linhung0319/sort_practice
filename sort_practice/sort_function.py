
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

if __name__ == '__main__':
    nums = [5, -1, 4, 2, 2]
    bubble_sort(nums)
    print(nums)