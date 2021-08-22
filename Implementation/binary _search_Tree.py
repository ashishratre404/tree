class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
        self.level = None # for top view

class Tree:
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
    
    # (left, root, right)
    def InOrder(self, root):
        if root is not None:
            self.InOrder(root.left)
            print(root.data)
            self.InOrder(root.right)

    # (root, left, right)
    def PreOrder(self, root):
        if root is not None:
            print(root.data)
            self.PreOrder(root.left)
            self.PreOrder(root.right)

    # (left, right, root)
    def PostOrder(self, root):
        if root is not None:
            self.PostOrder(root.left)
            self.PostOrder(root.right)
            print(root.data)

    
    # Height of binary tree
    def height(self, root):
        if root is None:
            return -1
        return max(self.height(root.left), self.height(root.right)) + 1

    # Diameter of binary tree
    def diameter(self, root):
        diameter = [0]

        def helper(root):
            if not root:
                return -1
            left = helper(root.left)
            right = helper(root.right)
            diameter[0] = max(diameter[0], 2 + left + right)
            return 1 + max(left, right)
        helper(root)
        return diameter[0]

    #Inverse tree or mirror of a tree
    def inverBinaryTree(self, root):
        if not root: return root

        root.left, root.right = root.right, root.left
        self.inverBinaryTree(root.left)
        self.inverBinaryTree(root.right)
        return root
    
    # Level Order Traversal
    def levelOrder(self, root):
        q = []
        q.append(root)
        while q:
            root = q.pop(0)
            print(root.data, end=' ')
            if root.left is not None:
                q.append(root.left)
            if root.right is not None:
                q.append(root.right)

    # Vertical order Traversal
    def verticalOrder(self, root):
        pass
    
    # top view
    def topview(self, root):
        q = []
        d = dict()
        root.level = 0  

        q.append(root)

        while q:
            root = q.pop(0)
            if root.level not in d:
                d[root.level] = root.data
            if root.left is not None:
                q.append(root.left)
                root.left.level = root.level - 1
            if root.right is not None:
                q.append(root.right)
                root.right.level = root.level + 1
        # dict will return list but we dont want list so used unpack operator '*'
        # print(*d.values()) 

        # we have to print left to right
        for i in sorted(d):
            print(d[i], end=' ')

    
    # check if tree is balanced or not
    def isBalanced(self, root):
        def helper(node):
            if not node:
                return (0, True)
            l_height, l_balance = helper(node.left)
            r_height, r_balance = helper(node.right)

            return (max(l_height, r_height) + 1, l_balance and r_balance and abs(l_height - r_height) <= 1)
        return helper(root)[1]








# Driver code
bst = Tree()
root = bst.createNode(5)
print("root -->", root.data)
bst.insertNode(root, 2)
bst.insertNode(root, 10)
bst.insertNode(root, 7)
bst.insertNode(root, 15)
bst.insertNode(root, 12)
bst.insertNode(root, 20)
bst.insertNode(root, 30)
bst.insertNode(root, 6)
bst.insertNode(root, 8)

# Traversal
print("In order -->")
bst.InOrder(root)
print('pre order -->')
bst.PreOrder(root)
print("post order -->")
bst.PostOrder(root)

# Level Order Traversal
print('level order ->')
bst.levelOrder(root)

# top view
print(" ")
print('top view -->')
bst.topview(root)

# height of tree
print("")
print('height -->')
print(bst.height(root))