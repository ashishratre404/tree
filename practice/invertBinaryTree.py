# Leetcode: 220. Invert Binary Tree

class Solution:
    def inverBinaryTree(self, root):
        if not root: return root

        root.left, root.right = root.right, root.left
        self.inverBinaryTree(root.left)
        self.inverBinaryTree(root.right)
        return root