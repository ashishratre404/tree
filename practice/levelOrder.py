# Leetcode: 102. binary tree level order traversal

import collections
from typing import Collection


class Solution:
    def levelOrder(self, root):
        q = collections.deque()
        ans = []
        q.append(root)
        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                ans.append(level)
        return ans
