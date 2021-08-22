# Leetcode: 230. Kth Smallest Element in a BST

class Solution:
    def KthSmallestS(self, root, k):
        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right