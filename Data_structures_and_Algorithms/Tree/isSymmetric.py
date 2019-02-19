# logic: to make sure that both are same
# teh same for checking if two trees are mirror images as we are checking the same tree and its other side
# we can do the same for two trees

def issymmetric(root):
    def ism(l,r):
        if not l and not r: return True # means both stopped at same time
        if l and r and l.val == r.val:
            return ism(l.left, r.right) and ism(l.right, r.left) # giving both the trees as inp and verifying at each step
        return False
    return ism(root,root)