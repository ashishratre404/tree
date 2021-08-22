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
        self.val = data 
        self.left = None
        self.right = None





class Solution:
    def lcaOFbt(self, root, p, q):
        self.ans = None
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            cur  = node == p or node == q

            if (left and right) or (cur and left) or (cur and right):
                self.ans = node
                return
            if left or right or cur:
                return True
        
        dfs(root)
        return self.ans


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
a = s.lcaOFbt(root, root.left.left, root.right)
print(a.val)