from sort_practice.sort_function import compare
class Heap():
    def __init__(self, nums=[], key=lambda x: x, reverse=False):
        self.__key = key
        self.__reverse = reverse
        self.heapify(nums)

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
            self.__array[x_parent_i], self.__array[x_i] = self.__array[x_i], self.__array[x_parent_i]
            x_i = x_parent_i
                
    def pop(self):
        pass

    def show(self):
        return self.__array