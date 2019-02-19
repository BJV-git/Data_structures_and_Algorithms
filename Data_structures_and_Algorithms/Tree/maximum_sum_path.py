# we can assume that it is going to be a tree path with root in generalized way
# so that is how we proceed further

# so why, we update at every node the self.max to see if that is the total max
# to cover the edge case - not considering the branch we push 0, i.e. the entire branch is neglected

class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
class solution():
    def maximum_path_sum(self,root):
        def maxi(root):
            if not root: return 0
            left = maxi(root.left)
            right = maxi(root.right)

            self.max = max(self.max, root.val + left+right)
            return max(root.val + max(left,right), 0)
        self.max = None
        maxi(root)
        return self.max