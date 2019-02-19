# logic: lets see if we have not root
# see if its leaf and summ == sum
# else pass the sum to left and right by subtracting

def haspathsum(root,summ):
    if not root: return False

    if not root.left and not root.right and root.val == summ:
        return True
    summ -= root.val

    return haspathsum(root.left, summ) or haspathsum(root.right, summ)