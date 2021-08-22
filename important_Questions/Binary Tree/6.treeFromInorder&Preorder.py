# Leetcode: 105. Construct binary trom inorde and preorder travesal

# - leftMost value (0-index) of preorder would be root
# - use that root in given inorder traversal, left of root would be left subtree and right be right subtree

class TreeNode:
    def __init__(self, val=None):
        self.right = None
        self.left = None
        self.val = val

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1 : ], inorder[mid+1 :])
        return root
    
    #checking
    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        print(root.val, end=' ')
        self.inorder(root.right)
    def preorder(self, root):
        if not root:
            return None
        print(root.val, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

s = Solution()
a = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
print('levelorder -->')
s.preorder(a)
print()
print('Inorder -->')
s.inorder(a)