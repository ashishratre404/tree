"""

            5
          /   \
        /      \
       2        7
     /  \      / \
    1    4    6   8

given:
    root.val in range(1, float('inf'))
deadend: node where appending child is not possible

approach:
 1. tc - O(n) and sc - O(n)
   - we can store leaf node and one set1 and other nodes in set2
   - check if, 'leafnode.val - 1' and 'leafnode.val + 1' in set2, if yes then we found dead-eand
 2. tc - O(n) and sc - O(1)
   - we can check minValue and maxValue for every node, if this is eqal then we cant add its child
   - initially minVAlue is 1 (given), and maxValue is infinity

"""
class Node:
    def __init__(self,data) -> None:
        self.val = data 
        self.left = None
        self.right = None

class Solution:
    def deadend(self, root):
        def isDeadend(root, minValue, maxValue):
            if not root:
                return False
            if minValue == maxValue:
                print(root.val)
                return True
            return isDeadend(root.left, minValue, root.val - 1) or isDeadend(root.right, root.val + 1, maxValue)
            
        
        return isDeadend(root, 1, float('inf'))


# Driver Code
root = Node(5)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

s = Solution()
a = s.deadend(root)
print(a)
