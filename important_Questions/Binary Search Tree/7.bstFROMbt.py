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



Construct BST from BT such that its structure should remain unchanged.
Approach:
    1. get inorder of bt
    2. sort that inorder
    3. change the node value of bt according to sorted inorder
"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None

class Solution:
    def bst_from_bt(self, root):
        self.inorder = []
        def inorderTraversal(node):
            if node:
                inorderTraversal(node.left)
                self.inorder.append(node.val)
                inorderTraversal(node.right)
            

        def replace(node):
            if node:
                replace(node.left)
                node.val = self.inorder[self.i]
                self.i += 1
                replace(node.right)
        
        inorderTraversal(root)
        self.inorder.sort()
        self.i = 0
        replace(root)
        


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

s = Solution()
s.bst_from_bt(root)
