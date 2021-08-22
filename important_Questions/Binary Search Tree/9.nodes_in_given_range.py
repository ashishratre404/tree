# count no. of nodes lies in range [l, h]

def countNodes(node, l, h):
    if not node: return 0
    if node.val >= l and node.val <=h:
        return 1 + countNodes(node.left, l, h) + countNodes(node.right, l, h)
    elif node.val < l:
        return countNodes(node.right, l, h)
    else:
        return countNodes(node.left, l, h)
