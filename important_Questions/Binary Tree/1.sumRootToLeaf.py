# Leetcode: 129.Sun Root to leaf Numbers
"""
        5
      /   \
    3      7
   / \    / \
  2   4  6   9

 return 532 + 534 + 576 + 579


"""

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
        self.level = None

class Solution:
    def createNode(self, data):
        return Node(data)

    def insertNode(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insertNode(node.left, data)
        else:
            node.right = self.insertNode(node.right, data)
        return node

    def sumNumbers(self, cur):
        def dfs(node, cur_sum):
            if not node:
                return 0
            cur_sum = cur_sum * 10 + node.data
            if not node.left and not node.right:
                print(cur_sum)
                return cur_sum
            return dfs(node.left, cur_sum) + dfs(node.right, cur_sum)

        return dfs(cur, 0)
            

bst = Solution()
root = bst.createNode(5)
bst.insertNode(root, 3)
bst.insertNode(root, 7)
bst.insertNode(root, 2)
bst.insertNode(root, 4)
bst.insertNode(root, 6)
bst.insertNode(root, 9)

print(bst.sumNumbers(root))