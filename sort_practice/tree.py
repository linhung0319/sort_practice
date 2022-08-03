from sort_practice.sort_function import compare
class Heap():
    def __init__(self, nums=[], key=lambda x: x, reverse=False):
        self.__key = key
        self.__reverse = reverse
        self.heapify(nums)

    def __len__(self):
        return len(self.__array)

    def _swap(self, left, right):
        self.__array[left], self.__array[right] = self.__array[right], self.__array[left]

    def heapify(self, nums):
        self.__array = []
        for x in nums:
            self.push(x)

    def push(self, x):
        self.__array.append(x)
        x_i = len(self.__array) - 1

        ### Stop adjusting the position of the pushed value
        ### x if the pushed value is already at the root.
        while x_i > 0:
            x_parent_i = (x_i - 1) // 2
            ### Stop adjusting the position of x, if 
            ### x is already in the correct position
            if not compare( self.__key(self.__array[x_parent_i]), 
                            self.__key(self.__array[x_i]), 
                            self.__reverse ):
                break
            ### If x is smaller than its parent, swap with its parent
            self._swap(x_parent_i, x_i)
            x_i = x_parent_i
                
    def pop(self):
        if not self.__array:
            return None
        ### When we delete the first element from
        ### a complete binary tree, we pop the last
        ### element x and place it at the first index
        ### of the array to keep a complete binary tree
        pop_v = self.__array[0]
        self.__array[0] = self.__array.pop()
        n = len(self.__array)
        x_i = 0
        ### Since x might not be in the heap order, we need to 
        ### check its child node and adjust the position of x
        ### to the correct place 
        while x_i * 2 + 1 < n:
            x_il = x_i * 2 + 1   ### left child node
            x_ir = x_i * 2 + 2   ### right child node
            ### Swap x with the left child node, if the left 
            ### child node exists and has the smallest value. 
            if x_ir < n and compare(self.__key(self.__array[x_il]), 
                                    self.__key(self.__array[x_ir]),
                                    self.__reverse):
                if  compare(self.__key(self.__array[x_i]), 
                            self.__key(self.__array[x_ir]),
                            self.__reverse):
                    self._swap(x_i, x_ir)
                    x_i = x_ir
                    continue
                ### If x doesn't need to swap, it is in 
                ### already in the correct position.
                break

            ### Swap x with the right child node, if the right 
            ### child node exists and has the smallest value.
            if compare(self.__key(self.__array[x_i]), 
                       self.__key(self.__array[x_il]),
                       self.__reverse):
                self._swap(x_i, x_il)
                x_i = x_il
                continue  
            ### If x doesn't need to swap, it is in 
            ### already in the correct position. 
            break
        return pop_v

    def show(self):
        return self.__array