

def all_leaves(root):
    if root:
        if not root.left and not root.right:
            print(root.val)
        all_leaves(root.left)
        all_leaves(root.right)