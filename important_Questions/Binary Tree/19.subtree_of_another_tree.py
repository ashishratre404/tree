# Leetcode: 572.Subtree of another tree
# Given: s,t are two non empty tree 
# check if t is subtree of s (s can also be subtree of  itself)

"""
        3                         4
       /  \                     /  \
      4    5       and         1    2
     /\   
    1  2     
    answer: Tree


        3                         4
       /  \                     /  \
      4    5       and         1    2
     /\   
    1  2 
      /
     8

    ans: False ( because two has extra descendats i.e. 8)    
 
"""

class solution:
    def isSubtree(self, s, t):
        if not s and not t: return True
        if not t: return True
        if not s and t: return False
        return self.isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    

    def isSame(self, s,t):
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
