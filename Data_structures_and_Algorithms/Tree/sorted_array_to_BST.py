# learned logic: again we can go by divide and conquer

# so this is an opposite if an inorder traversal

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortarrayBST(nums):
    def convert(left,right):
        if left>right:
            return
        mid = (left+right)//2
        node = TreeNode(nums[mid])

        node.left = convert(left, mid-1)
        node.right = convert(mid+1, right)
        return node
    return convert(0,len(nums)-1)