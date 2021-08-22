
class Node:
    def __init__(self, val = None) -> None:
        self.left = None
        self.right = None
        self.val = val


class Solution:
    def mirrorTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.mirrorTree(p.left, q.right) and self.mirrorTree(p.right, q.left))
    

#driver code
p = Node(3)
p.left = Node(41)
p.right = Node(9)

q = Node(3)
q.left = Node(9)
q.right = Node(0)

s = Solution()
a = s.mirrorTree(p, q)
print(a)