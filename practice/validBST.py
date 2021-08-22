# Leetcode: 98. valid binary search tree


# Note: we can also apply inorder traversal, inorder traversal of bst gives values in sorted order
class Solution:
    def validBST(self, node):
        def helper(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return (helper(node.left, left, node.val) and helper(node.right, node.val, right))
        
        return helper(node, float('-inf'), float('inf'))

        