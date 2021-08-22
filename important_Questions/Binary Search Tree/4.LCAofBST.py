# Leedcode: 235.Lowest Common Ancestor of bst

# (1) if root.val is smaller than one of p and q and larger than other one then where the split occure that node is LCA
# (2) if both p and q is larger than root.val then we have to check for right subtree and get node where split coccured
# (3) if p and q is smaller then do same with left subtree 
# (4) if one of p and q is equal to root.val then this root is LCA

class Solution:
    def LCAofBST(self, root, p, q):
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val: #(2)
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: #(3)
                cur = cur.left
            else:  # (1) and (4)
                return cur

            