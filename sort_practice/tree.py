from abc import ABC, abstractmethod
from sort_practice.sort_function import compare
class Heap():
    def __init__(self, nums=[], key=lambda x: x, reverse=False):
        self.__key = key
        self.__reverse = reverse
        self.__array = []
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
        n = len(self.__array)
        if n == 1:
            return self.__array[0]

        pop_v = self.__array[0]
        self.__array[0] = self.__array.pop()
        n -= 1
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

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class AVLTreeNode(TreeNode):
    def __init__(self, val):
        super(AVLTreeNode, self).__init__(val)
        self.height = 1

class BinaryTree(ABC):
    def __init__(self, nums):
        self._root = None
        self.build(nums)

    @abstractmethod
    def make_node(self, x) -> TreeNode:
        raise NotImplementedError()

    @abstractmethod
    def search(self, x):
        raise NotImplementedError()

    @abstractmethod
    def insert(self, x):
        raise NotImplementedError()

    @abstractmethod
    def delete(self, x):
        raise NotImplementedError()

    def build(self, nums):
        ### Clear all nodes in the tree
        self._root = None
        for num in nums:
            self.insert(num)

    def inorder(self, reverse=False):
        array = []
        def helper(root: TreeNode):
            if not root:
                return
            helper(root.left)
            array.append(root.val)
            helper(root.right)

        def helper_reverse(root: TreeNode):
            if not root:
                return
            helper_reverse(root.right)
            array.append(root.val)
            helper_reverse(root.left)

        if reverse:
            ### Append the tree into array in RDL order
            helper_reverse(self._root)
        else:
            ### Append the tree into array in LDR order 
            helper(self._root)
        return array

class BinarySearchTree(BinaryTree):
    def __init__(self, nums=[], key=lambda x: x):
        self._key = key
        super(BinarySearchTree, self).__init__(nums)

    def make_node(self, x):
        return TreeNode(x)

    def search(self, x):
        curr = self._root
        while True:
            if curr is None or self._key(curr.val) == self._key(x):
                return curr
            elif self._key(curr.val) < self._key(x):
                ### If x > current node, search the right child node.
                curr = curr.right
            else:
                ### If x < current node, search the left child node.
                curr = curr.left

    def insert(self, x):
        new_node = self.make_node(x)
        if not self._root:
            self._root = new_node
            return

        ### Complare the new node with nodes in binary search tree.
        ### If the new node is larger than node A, go to the right 
        ### node of node A and vice versa. Repeat this process until 
        ### we find an empty node.
        curr = self._root
        while True:
            if self._key(curr.val) < self._key(new_node.val):
                ### If the node is empty, insert the new node
                if not curr.right:
                    curr.right = new_node
                    return
                ### If the node is not empty, search another node.
                curr = curr.right
            else:
                ### If the node is empty, insert the new node
                if not curr.left:
                    curr.left = new_node
                    return
                ### If the node is not empty, search another node.
                curr = curr.left 
        
    def delete(self, x):
        ### root is the representative of a tree.
        ### Return the root of a tree in which 
        ### we have already deleted x. 
        def helper(root, x):
            if root is None:
                return root

            if self._key(root.val) < self._key(x):
                root.right = helper(root.right, x)
            elif self._key(root.val) > self._key(x):
                root.left = helper(root.left, x)
            else:
                if root.left is None and root.right is None:
                    return None
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left

                ### Find the max value node 
                ### in the left subtree 
                curr = root.left
                while curr.right:
                    curr = curr.right

                ### Copy the left subtree max value to
                ### the current node. Now, we need to
                ### delete the max value node in the left
                ### subtree, since this node is dulplicated
                root.val = curr.val
                root.left = helper(root.left, curr.val)

            return root

        self._root = helper(self._root, x)

class AVLTree(BinarySearchTree):
    def make_node(self, x):
        return AVLTreeNode(x)

    def insert(self, x):
        ### root is the representative of a tree.
        ### Return the root of a tree in which 
        ### we have already inserted x. 
        def helper(root, x):
            ### Complare x with nodes in the tree. If x is larger 
            ### than root, the right subtree of root is updated to
            ### a tree in which x is inserted and vice versa.  
            if not root:
                return self.make_node(x)
            elif self._key(root.val) < self._key(x):
                root.right = helper(root.right, x) 
            else:
                root.left = helper(root.left, x)
        
            ### After we update the left or right subtree of root,
            ### we need to update the height of root.
            root.height = 1 + max( self.get_height(root.left), 
                                   self.get_height(root.right) )

            ### After we update the left or right subtree of root,
            ### we need to check the balance of root.
            balance = self.get_balance(root)

            ### If the balance is greater than 1 or smaller than
            ### -1, we need to re-balance the tree.
            ### Case 1 - left left
            if balance > 1 and self._key(x) < self._key(root.left.val):
                return self.right_rotate(root)
            ### Case 2 - left right
            if balance > 1 and self._key(x) > self._key(root.left.val):
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
            ### Case 3 - right right
            if balance < -1 and self._key(x) > self._key(root.right.val):
                return self.left_rotate(root)
            ### Case 4 - right left
            if balance < -1 and self._key(x) < self._key(root.right.val):
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
            
            ### If root is balance, we simply return root.
            return root

        self._root = helper(self._root, x)
        
    def delete(self, x):
        ### root is the representative of a tree.
        ### Return the root of a tree in which 
        ### we have already deleted x. 
        def helper(root, x):
            ### Complare x with nodes in the tree. If x is larger 
            ### than root, the right subtree of root is updated to
            ### a tree in which x is deleted and vice versa. 
            if not root:
                return root
            if self._key(root.val) < self._key(x):
                root.right = helper(root.right, x)
            if self._key(root.val) > self._key(x):
                root.left = helper(root.left, x)
            if self._key(root.val) == self._key(x):
                if root.left is None and root.right is None:
                    return None
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left

                ### Find the max value node 
                ### in the left subtree 
                curr = root.left
                while curr.right:
                    curr = curr.right

                ### Copy the left subtree max value to
                ### the current node. Now, we need to
                ### delete the max value node in the left
                ### subtree, since this node is dulplicated
                root.val = curr.val
                root.left = helper(root.left, curr.val)

            ### After we update the left or right subtree of root,
            ### we need to update the height of root.
            root.height = 1 + max( self.get_height(root.left), 
                                   self.get_height(root.right) )

            ### After we update the left or right subtree of root,
            ### we need to check the balance of root.
            balance = self.get_balance(root)

            ### If the balance is greater than 1 or smaller than
            ### -1, we need to re-balance the tree.
            ### Case 1 - left left
            if balance > 1 and self._key(x) > self._key(root.left.val):
                return self.right_rotate(root)
            ### Case 2 - left right
            if balance > 1 and self._key(x) < self._key(root.left.val):
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
            ### Case 3 - right right
            if balance < -1 and self._key(x) < self._key(root.right.val):
                return self.left_rotate(root)
            ### Case 4 - right left
            if balance < -1 and self._key(x) > self._key(root.right.val):
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
            
            ### If root is balance, we simply return root.
            return root
        
        self._root = helper(self._root, x)

    def get_height(self, node: AVLTreeNode):
        if not node:
            return 0
        return node.height

    def get_balance(self, node: AVLTreeNode):
        ### Balance is the height differce between the
        ### left subtree and right subtree. 
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def left_rotate(self, root: AVLTreeNode) -> AVLTreeNode:
        ### Perform rotation
        right_child = root.right
        root.right = right_child.left
        right_child.left = root

        ### Update heights
        root.height = 1 + max( self.get_height(root.left), 
                               self.get_height(root.right) )
        right_child.height = 1 + max( self.get_height(right_child.left), 
                                      self.get_height(right_child.right) )

        return right_child

    def right_rotate(self, root: AVLTreeNode) -> AVLTreeNode:
        ### Perform rotation
        left_child = root.left
        root.left = left_child.right
        left_child.right = root

        ### Update heights
        root.height = 1 + max( self.get_height(root.left), 
                               self.get_height(root.right) )
        left_child.height = 1 + max( self.get_height(left_child.left), 
                                     self.get_height(left_child.right) )
        return left_child