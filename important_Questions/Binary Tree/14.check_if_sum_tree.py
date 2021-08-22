"""

            1
          /   \
        /      \
       2        3
     /  \      / \
    4    5    6   7


            44
          /   \
        /      \
       9        13
     /  \      / \
    4    5    6   7

Note: assume leaf node to be already a sum tree

"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None


class Solution:
    def isSumTree(self, root):
        self.flag = 1
        def helper(root):
            if not root: return 0
            if not root.left and not root.right:
                return root.val
            if self.flag == 0:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            if (left + right) != root.val:
                self.flag = 0
            return left + right + root.val
        helper(root)
        return self.flag == 1
    


# Driver Code
root = Node(44)
root.left = Node(9)
root.right = Node(13)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
s = Solution()
a = s.isSumTree(root)
print(a)
