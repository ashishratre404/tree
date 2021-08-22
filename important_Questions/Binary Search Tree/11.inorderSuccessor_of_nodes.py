"""
every node has three pointer: left, right, next
task: point 'next' to its inorder successor

            5
          /   \
        /      \
       2        7
     /  \      / \
    1    4    6   8
        /
       3

prev -> 1, 1
"""
class Node:
    def __init__(self, val=None) -> None:
        self.val = val 
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def inorderSuccessor(self, root):
        def solve(root, prev):
            if root:
                solve(root.left, prev)
                if prev.val is None:
                    prev.next = root
                prev = root
                solve(root.right, prev)
        
        prev = Node()
        solve(root, prev)
        



# Driver Code
root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.right.left = Node(3)

s = Solution()
s.inorderSuccessor(root)
print(root.next.val)
