"""

            1
          /   \
        /      \
       2        3
     /  \      / \
    4    5    6   7

inorder befor converting into sum tree: 4, 2, 5, 1, 6, 3, 7
inorder after converting into sum tree: 0, 9, 0, 27, 0, 13, 0

sum tree: every node contains sum of its left sub-tree and right sub-tree  (leaf nodes are 0 because ifs child contains None)

"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None


class Solution:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)

    def bt2sumtree(self, root):
        if not root: return 0
        
        left = self.bt2sumtree(root.left)
        right = self.bt2sumtree(root.right)
        rootValue = root.val
        root.val = left + right
        return left + right + rootValue


# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


s = Solution()
s.inorder(root)
print()
s.bt2sumtree(root)
print()
s.inorder(root)