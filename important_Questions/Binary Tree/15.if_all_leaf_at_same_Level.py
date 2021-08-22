"""

            1
          /   \
        /      \
       2        3
     /  \      / \
    4    5    6   7

"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None


class Solution:
    def isSameLevel(self, root):
        self.res = None
        self.ans = True

        def helper(node, level):
            if not node: return
            if not node.left and not node.right:
                if self.res == None:
                    self.res = level
                else:
                    if self.res != level:
                        self.ans = False
                return
            if self.ans == False:
                return
            l = helper(node.left, level+1)
            r = helper(node.right, level+1)
        helper(root, 0)
        return self.ans


        


# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)


s = Solution()
b = s.isSameLevel(root)
print(b)
