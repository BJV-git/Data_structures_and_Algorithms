def find_min_path(root):
    if not root: return 0

    l = find_min_path(root.left)
    r = find_min_path(root.right)

class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
class solution():
    def maximum_path_sum(self,root):
        def mini(root):
            if not root: return 0
            left = mini(root.left)
            right = mini(root.right)

            self.min = min(self.min, root.val + left+right)
            return min(root.val + min(left,right), 0)
        self.min = None
        mini(root)
        return self.min