# keep an eye on the last nodes so retunr 0, when taken diff return the hight
# if seen diff return -1 and to check see if there are any -1, so that retunr recursively

def isBalanced(root):
    def check(root):
        if not root: return 0
        left = check(root.left)
        right = check(root.right)

        if left ==-1 or right == -1 or  abs(left-right) >1:
            return -1
        return 1+max(left, right)

    return check(root)