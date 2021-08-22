"""

            1
          /   \
        /      \
       2        3
     /  \      / \
    4    5    6   7
        /
       8
      /
    9
   /
  10

"""
class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.left = None
        self.right = None

class BinaryTree:
    def insert(self, root):
        pass
    # InOrder (left, root, right)
    def InOrder(self, root):
        if root is not None:
            self.InOrder(root.left)
            print(root.data)
            self.InOrder(root.right)
    
    #PreOrder (root, left, right)
    def PreOrder(self, root):
        if root is not None:
            print(root.data)
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    # PostOrder (left, right, root)
    def PostOrder(self, root):
        if root is not None:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.data)
    
    # Height of binary tree
    def height(self, root):
        if not root:
            return -1
        return max(self.height(root.left), self.height(root.right)) + 1 

     # Diameter of binary tree
    def diameter(self, root):
        diameter = [0]

        def helper(root):
            if not root:
                return -1
            left = helper(root.left)
            right = helper(root.right)
            diameter[0] = max(diameter[0], 2 + left + right)
            return 1 + max(left, right)
        helper(root)
        return diameter[0]
    
    # Mirror of tree
    def mirror(self, root):
        if not root: return root

        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
        return root

    # level order travesal
    #   1. direct values from top to bottom 
    #   2. values in list of list according to level
    def levelOrder(self, root):
        if not root:
            return root
        q = [root]
        while q:
            root = q.pop(0)
            print(root.data, end=" ")
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
    def levelOrderList(self, root):
        q = []
        next_q = []
        res = []
        level = []
        if not root:
            return root
        q.append(root)
        while q:
            for root in q:
                level.append(root.data)
                if root.left:
                    next_q.append(root.left)
                if root.right:
                    next_q.append(root.right)
            res.append(level)
            level = []
            q = next_q
            next_q = []
        return res

    # searching a value
    def serchingValue(self, root, serchingData):
        if not root:
            return False
        else:
            inLeft = self.serchingValue(root.left, serchingData)
            inRight = self.serchingValue(root.right, serchingData)
            print(root.data, inLeft, inRight)
            return root.data == serchingData or inLeft or inRight
    
    # Max value of binary Tree
    def maxVal(self, root):
        if root is None:
            return float("-inf")
        else:
            leftMax = self.maxVal(root.left)
            rightmax = self.maxVal(root.right)
            return max(root.data, leftMax, rightmax) 

    # check if tree is balanced or not
    def isBalanced(self, root):
        def helper(node):
            if not node:
                return (0, True)
            l_height, l_balance = helper(node.left)
            r_height, r_balance = helper(node.right)

            print(node.data)
            return (max(l_height, r_height) + 1, l_balance and r_balance and abs(l_height - r_height) <= 1)
        return helper(root)[1]
        



    



# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.left.left = Node(9)
root.left.right.left.left.left = Node(10)

bt = BinaryTree()
a = bt.levelOrderList(root)
print(a)

