# just traverse and update the sum
# better if gone with the post order traversal

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class solution():

    def findlargestsum(self, root):

        if not root: return 0
        currsum= (root.val + self.findlargestsum(root.left) + self.findlargestsum(root.right))
        self.maxi = max(self.maxi, currsum)
        return currsum

    # return findlargestsum(root)