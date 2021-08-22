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
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None


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
