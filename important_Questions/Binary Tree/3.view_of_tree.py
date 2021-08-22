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
   

  top view: 10,4,2,1,3,7
  right view: 1,3,7,8,9,10
  left view: 1,2,4,8,9,10
  bottom view: 10,9,8,5,6,,7

"""
import collections

class CreateNode:
    def __init__(self, val=None) -> None:
        self.val = val 
        self.left = None
        self.right = None
        self.level = None

class Solurion:
    # top view
    def topView(self, root):
        q = []
        d = dict()
        q.append(root)
        root.level = 0
        while q:
            root = q.pop(0)
            if root.level not in d:
                d[root.level] = root.val
            if root.left:
                q.append(root.left)
                root.left.level = root.level - 1
            if root.right:
                q.append(root.right)
                root.right.level = root.level + 1
        
        for i in sorted(d):
            print(d[i], end=' ')


    # Right View
    # Leetcode: 199. Binary Tree Right Side View
    def rightView(self, root):
        res = []
        q = collections.deque([root])

        while q:
            rightMost = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightMost = node.val
                    q.append(node.left)
                    q.append(node.right)
            if rightMost is not None:
                res.append(rightMost)
        return res
            
root = CreateNode(1)
root.left = CreateNode(2)
root.right = CreateNode(3)
root.left.left = CreateNode(4)
root.left.right = CreateNode(5)
root.right.left = CreateNode(6)
root.right.right = CreateNode(7)
root.left.right.left = CreateNode(8)
root.left.right.left.left = CreateNode(9)
root.left.right.left.left.left = CreateNode(10)


v = Solurion()
a = v.rightView(root)
print(a)