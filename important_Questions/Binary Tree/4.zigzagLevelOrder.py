"""
Leetcode: 203. Binary tree zigzag level order traversal
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
zigzag level order: [[1], [3,2], [4,5,6,7], [8], [9], [10]]
"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None

class Solution:
    def zigzaglevelorder(self, root):
        if not root: return root
        evenLevel = [root]
        oddLevel = []
        level = []
        result = []

        while evenLevel or oddLevel:
            while evenLevel:
                root = evenLevel.pop()
                level.append(root.val)
                if root.left:
                    oddLevel.append(root.left)
                if root.right:
                    oddLevel.append(root.right)
            result.append(level)
            level = []

            while oddLevel:
                root = oddLevel.pop()
                level.append(root.val)
                if root.right: #right first then left (because we need to work in zigzag manner)
                    evenLevel.append(root.right)
                if root.left:
                    evenLevel.append(root.left)
    
            if level != []:
                result.append(level)
                level = []
        return result
    

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
a = s.zigzaglevelorder(root)
print(a)