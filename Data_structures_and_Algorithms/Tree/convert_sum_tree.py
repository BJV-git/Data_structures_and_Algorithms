# can write recursion, if leaf lets assign 0 adn return teh value, else node.val = sum(lef + sum(rught
# better to return the sum of sum and  then the current value fo the node as we dont want to miss that


def convertSumTree(root):
    if not root: return None

    if not root.left and not root.right:
        valu = root.val
        root.val = 0
        return valu

    valu = root.val
    root.val = convertSumTree(root.left) + convertSumTree(root.right)
    return valu