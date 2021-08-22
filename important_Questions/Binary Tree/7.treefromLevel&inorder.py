# Leetcode: 105. Construct binary trom inorde and preorder travesal

# - leftMost value (0-index) of levelorder would be root
# - use that root in given inorder traversal, left of root would be left subtree and right be right subtree

class TreeNode:
    def __init__(self, val=None):
        self.right = None
        self.left = None
        self.val = val

class Solution:
    def buildTree(self, levelorder, inorder):
        if not levelorder and not inorder:
            return None
        root = TreeNode(levelorder[0])
        mid = inorder.index(levelorder[0])
        root.left = self.buildTree(levelorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(levelorder[mid+1 : ], inorder[mid+1 :])
        return root
    
    #checking
    def inorder(self, root):
        if not root:
            return None
        self.inorder(root.left)
        print(root.val, end=' ')
        self.inorder(root.right)
    def levelorder(self, root):
        if not root:
            return None
        q = [root]
        while q:
            root = q.pop(0)
            print(root.val, end=' ')
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        

s = Solution()
a = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
print('preorder -->')
s.preorder(a)
print()
print('Inorder -->')
s.inorder(a)