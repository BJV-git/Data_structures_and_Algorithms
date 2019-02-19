# we will split the inorder and add to the output only if while splitting the in order list has mpre than 1 len
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder , inorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left =  buildTree(preorder, inorder[:ind])
        root.right = buildTree(preorder, inorder[ind+1:])
        return root