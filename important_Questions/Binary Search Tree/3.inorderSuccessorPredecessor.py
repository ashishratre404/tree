"""

            1
          /   \
        /      \
       2        3
     /  \      / \
    4    5    6   7
        /
       8
      /
    9
   /
  10

"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None

class Solurion:
    def succAndpred(self, root,pre,succ, key):
        def inpre(root):
            p = root.left
            while p:
                p = p.left
            return p.val
        def insuc(root):
            s = root.right
            while s:
                s = s.right
            return s.val


        if not root: return 
        if root.val == key:
            if root.left: 
                pre = inpre(root)
            if root.right:
                succ = insuc(root)
            return
        if key > root.val:
            pre = root.val
            self.succAndpred(root.right, pre, succ, key)
        if key < root.val:
            succ = root.val
            self.succAndpred(root.left, pre, succ, key)





# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.left.left = Node(9)
root.left.right.left.left.left = Node(10)


s = Solurion()
a = s.succAndpred(root, None, None, 5)
print(a)