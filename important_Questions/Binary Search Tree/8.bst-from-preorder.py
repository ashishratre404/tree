"""

            5
          /   \ 
        /      \ 
       2        7
     /  \      / \ 
    1    4    6   8

preorder: 5,2,1,4,7,6,8
"""

class Node:
    def __init__(self, val = None) -> None:
        self.left = None
        self.right = None
        self.val = val

class Solution:
    def bstFromPreorder(self, preorder):
        stack = []
        N = len(preorder)
        root = Node(preorder[0])
        stack.append(root)
        for i in range(1, N):
            if preorder[i] < stack[-1].val:
                stack[-1].left = Node(preorder[i])
                stack.append(stack[-1].left)
            
            else:
                while stack and preorder[i] > stack[-1].val:
                    last = stack.pop()
                last.right = Node(preorder[i])
                stack.append(last.right)
        return root
    
    #checking: given preorder should be same to preorder of tree we made
    def preorderTraversal(self, node):
        if node:
            print(node.val, end=' ')
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)



# Driver Code
root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

s = Solution()
a = s.bstFromPreorder([5,2,1,4,7,6,8])
s.preorderTraversal(a)