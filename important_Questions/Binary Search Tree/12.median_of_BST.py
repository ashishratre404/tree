"""

            5
          /   \
        /      \
       2        7
     /  \      / \
    1    4    6   8

median:
   for odd: median = (n/2) + 1
   for even: median = ((n/2) + ((n/2) + 1)) / 2

two approach:
    1. traverse inorder and sotre and use the formula for median [ tc - O(n), sc - O(n)]

"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None

class solution:
    def medianBST(self, root):
        pass



# Driver Code
root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
