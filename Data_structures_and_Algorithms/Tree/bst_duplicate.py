# can go for inorder and see if prev == presnrt

def bst_duplicate(root):
    prev = []

    def inorder(root):
        if root:
            inorder(root.left)
            if prev[0] ==root.val:
                return True
            prev[0] = root.val
            inorder(root.right)
    res = inorder(root)
    if res:
        return res
    else:
        return False