# logic: the same has to be used while building because, once we place a node means that all the nodes left and right obey the
# rules

def isValidBST(self, root, less=float('-inf'), great=float('inf')):
    if not root:
        return True
    if root.val >= less or root.val <= great:
        return False
    return self.isValidBST(root.left, min(root.val, less), great) and self.isValidBST(root.right, less,
                                                                                      max(root.val, great))