"""

            5                                      4
          /   \                                  /   \
        /      \                               2      7
       2        7         =>                  / \    /
     /  \                                    1  3   5
    1    4    
        /
       3

       BST                                 Balanced BST

inorder: 1,2,3,4,5,7
"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None


class Solution:
    def bst_balancedBST(self, root):
        self.inorder = []
        def inorderTraversal(node):
            if node:
                inorderTraversal(node.left)
                self.inorder.append(node.val)
                inorderTraversal(node.right)
        
               
        def balnceBST(inorder):
            mid = len(inorder)//2
            if len(inorder) > 0:
                root = Node(inorder[mid])
                root.left = balnceBST(inorder[:mid])
                root.right = balnceBST(inorder[mid+1:])
                return root
        
        inorderTraversal(root)
        return balnceBST(self.inorder)




# Driver Code
root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(4)
root.left.right.left = Node(3)

s = Solution()
a = s.bst_balancedBST(root)
print(a.val)
print(a.left.val)
print(a.right.val)
print(a.left.left.val)
print(a.left.right.val)
print(a.right.left.val)

