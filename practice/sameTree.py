# Leetcode: 100. Same Tree
class Solution:
    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.sameTree(p.left, q.left)) and (self.sameTree(p.right, q.right))

        