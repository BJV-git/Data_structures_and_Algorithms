class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def smallest_value_BST(root):
    if not root: return None
    if root.left is None:
        return root.val

    else:
        return smallest_value_BST(root.left)