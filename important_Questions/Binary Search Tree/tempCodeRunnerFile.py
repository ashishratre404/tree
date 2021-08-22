    root = Node(inorder[mid])
                print(root.val)
                root.left = balnceBST(inorder[:mid])
                root.right = balnceBST(inorder[mid+1:])
                return root