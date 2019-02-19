# just concatnate all the paths and verify the sum value

class solution(object):

    def __init__(self):
        self.paths=[]

    def pathsum(self, root, summ, currentpath=None):
        if root:
            if currentpath==None: currentpath=[]
            currentpath.append(root.val)

            if not root.left and root.right and summ-root.val ==0:
                self.paths.append(currentpath)
                return self.paths
            self.pathsum(root.left, summ-root.val, currentpath)
            self.pathsum(root.right, summ - root.val, currentpath)

        return self.paths