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
    def __init__(self,data=None) -> None:
        self.val = data 
        self.left = None
        self.right = None

class Solution:
    def bt2dll(self, root, cur,head, f):  
        if not root: return root
        def inorder(root, cur, head, f):

            if root:
                inorder(root.left, cur, head, f)
                a = Node(root.val)
                if f == 0:
                    cur = a
                    head = a
                    f = 1
                else:
                    cur.rihgt = a
                    a.left = cur
                    cur = cur.right               
                inorder(root.right, cur, head, f)
            return head

        def displayDLL(head):
            while head:
                print(head.val, end=' ')
                head = head.right  

        
        a = inorder(root, cur, head, f)
        return displayDLL(a)




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



head = Node(0)
cur = head
f = 0
s = Solution()
s.bt2dll(root, cur, head, f)