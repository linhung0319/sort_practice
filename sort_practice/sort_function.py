
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
        
def insertion_sort(nums, key=lambda x: x, reverse=False):
    n = len(nums)
    ### The first element is assumed to be sorted,
    ### so we start from the second element.
    for i in range(1, n):
        ### place the unsorted element nums[i]
        ### at the correct position in the 
        ### sorted part of array  
        for j in range(i - 1, -1, -1):
            ### If the unsorted element need to insert to
            ### the left of the sorted elements, the sorted
            ### element need to shift by one to the right
            if compare(key(nums[j]), key(nums[j+1]), reverse):
                nums[j], nums[j+1] = nums[j+1], nums[j]
            else:
                ### The correct position of the unsorted
                ### element is just behind the value 
                ### smaller than it
                continue

def merge_sort(nums, key=lambda x: x, reverse=False):
    ### merge_op can merge two sorted 
    ### parts into a merge sorted array
    def merge_op(l1, r1, l2, r2):
        tmp = []
        start = l1
        end = r2
        ### Take the smaller value from both parts and 
        ### store it in tmp that will hold the findal answer
        while l1 <= r1 and l2 <= r2:
            if compare(key(nums[l1]), key(nums[l2]), reverse):
                tmp.append(nums[l2])
                l2 += 1
            else:
                tmp.append(nums[l1])
                l1 += 1
        while l1 <= r1:
            tmp.append(nums[l1])
            l1 += 1
        while l2 <= r2:
            tmp.append(nums[l2])
            l2 += 1
        nums[start:end + 1] = tmp

    ### Consider a single element as a sorted part.
    n = len(nums)
    sorted_len = 1
    while sorted_len <= n:
        ### perform merge_op on two sorted parts
        sorted_len_2 = sorted_len * 2
        for i in range(0, n, sorted_len_2):
            l1 = i
            r1 = i + sorted_len - 1
            l2 = i + sorted_len
            r2 = i + sorted_len_2 - 1
            ### If no second sorted part remains,
            ### merge_op is not required
            if l2 >= n:
                break
            ### the second sorted part remains,
            ### but the actual lenght is smaller
            ### than sorted_len.
            if r2 >= n:
                r2 = n - 1
            merge_op(l1, r1, l2, r2)
        sorted_len = sorted_len_2
        
def quick_sort(nums, key=lambda x: x, reverse=False):
    def partition(left, right):
        pivot = nums[right]
        pivot_i = left
        for i in range(left, right + 1):
            if not compare(key(nums[i]), key(pivot), reverse):
                nums[i], nums[pivot_i] = nums[pivot_i], nums[i]
                pivot_i += 1
    partition(0, 4)


    

if __name__ == '__main__':
    nums = [5, -1, 4, 2, 2]
    #nums = [-1, 0, 1, -1, 5]
    #bubble_sort(nums)
    #selection_sort(nums)
    #insertion_sort(nums)
    #merge_sort(nums)
    quick_sort(nums)
    print(nums)