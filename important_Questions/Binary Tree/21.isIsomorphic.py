
# isomorphic: if tree is same or if it become same if swape left and right

class Solution:
    def isIsomorphic(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        a = self.isIsomorphic(p.left, q.left) and self.isIsomorphic(p.right, q.right) # if both are same
        b = self.isIsomorphic(p.left, q.right) and self.isIsomorphic(p.right, q.left) # if both became same after swapping
        return a or b
        
