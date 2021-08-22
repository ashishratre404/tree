# Leetcode: 124. Binary Tree Path Sum

class Solution:
    def maxPathSum(self, root):
        res = [root.val] # this will be keep on updating with max path sum

        def dfs(root):
            if not root: return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0) #checking with 0 because of negative value is also possible

            
            res[0] = max(res[0], root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]
