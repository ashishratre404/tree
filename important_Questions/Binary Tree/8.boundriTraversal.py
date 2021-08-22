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
boundry traversal : 1,2,4,10,6,7,3
leftnodes( atleast contain one child) then child nodes (left and right are none) then right nodes (revese)
"""
class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.left = None
        self.right = None

class Solution:   
    def boundry(self, root):
        if not root:
            return None
        def leftNodes(root, ans):
            if not root:
                return
            if root.left:
                ans.append(root.data)
                leftNodes(root.left, ans)
            elif root.right:
                ans.append(root.data)
                leftNodes(root.right, ans)
        
        def leafNodes(root, ans):
            if not root:
                return
            leafNodes(root.left, ans)
            if not root.left and not root.right:
                ans.append(root.data)
            leafNodes(root.right, ans)
        
        def rightNodes(root, ans):
            if not root:
                return
            if root.right:
                rightNodes(root.right, ans)
                ans.append(root.data)
            elif root.left:
                rightNodes(root.left, ans)
                ans.append(root.data)
            
    
        ans = [root.data]
        leftNodes(root.left, ans)
        leafNodes(root, ans)
        rightNodes(root.right, ans)
        return ans



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
s = Solution()
a = s.boundry(root)
print(a)
