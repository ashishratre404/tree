# Leetcode: 98. valid binary search tree

class Solution:
    def validBST(self, root):
        def helper(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return (helper(node.left, left, node.val) and helper(node.right, node.val, right))


        return helper(root, float('-inf'), float('inf'))