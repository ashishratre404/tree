# Leetcode: 113. Path sum II

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def helper(self, root, cur_sum, lst, res):
        if root.left is None and root.right is None:
            if root.val == cur_sum:
                res = [lst + [root.val]]
        if root.left:
            self.helper(root.left, cur_sum - root.val, lst + [root.val], res)
        if root.right:
            self.helper(root.right, cur_sum - root.val, lst + [root.val], res)
        return res

    def pathSumII(self, root, sum):
        if not root:
            return root
        return self.helper(root, sum, [], [])

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.right.left = TreeNode(8)
root.left.right.left.left = TreeNode(9)
root.left.right.left.left.left = TreeNode(10)

s = Solution()
a = s.helper(root, 11, [],[])
print(a)