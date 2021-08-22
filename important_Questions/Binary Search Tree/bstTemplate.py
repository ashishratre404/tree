"""

            5
          /   \
        /      \
       2        7
     /  \      / \
    1    4    6   8
        /
       3

"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None


# Driver Code
root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)
root.left.right.left = Node(3)

