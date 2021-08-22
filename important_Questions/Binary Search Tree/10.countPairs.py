# count no. pairs whose sum is equal to X, we have to take one-one node.val from both tree

# two Approach: 
#    1. TC - O(m+n) st- O(m)
#     a) store any of tree in dict
#     b) travese in another tree and search for (x - node.val) in dict

#   2. TC- o(n*log(n)), st- o(1)
#     a) travese in any tree and search for (x - node.val) in another bst


class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None


class Solution:
    def coutPair(self, root1, root2, X):
        self.count = 0

        def isContain(node, k):
            if not node:
                return False
            if k == node.val:
                return True
            p = False
            q = False
            if k < node.val:
                p = isContain(node.left, k)
            if k > node.val:
                q = isContain(node.right, k)
            return p or q


        def inorder(root, root2, X):
            if root:
                inorder(root.left, root2, X)
                if isContain(root2, X - root.val):
                    self.count += 1
                inorder(root.right, root2, X)


        inorder(root1, root2, X)
        return self.count



# Driver Code
root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)


rooot = Node(9)
rooot.left = Node(6)
rooot.right = Node(14)
rooot.left.left = Node(5)
rooot.left.right = Node(8)
rooot.right.left = Node(13)
rooot.right.right = Node(25)


s = Solution()
a = s.coutPair(root, rooot, 12)
print(a)