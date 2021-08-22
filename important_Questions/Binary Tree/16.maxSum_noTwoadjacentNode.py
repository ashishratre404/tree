"""

            1
          /   \
        /      \
       2        3
     /  \      / \
    4    5    6   7
    

"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None

class Solution:
    def maxSum(self, root):
        dp = {}
        def helper(root):
            if not root: return 0
            if root in dp:
                return dp[root]
            
            #if including the root
            inc = root.val
            if root.left:
                inc += helper(root.left.left)
                inc += helper(root.left.right)
            if root.right:
                inc += helper(root.right.left)
                inc += helper(root.right.right)

            # if not including the root node
            exc = helper(root.left) + helper(root.right)
            dp[root] = max(inc, exc)

            return dp[root]
        return helper(root)



# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

s = Solution()
a = s.maxSum(root)
print(a)
