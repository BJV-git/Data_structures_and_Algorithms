# using the prev logic; if left and right has then set the flag and move on

def lcabinarytree(root,p,q):

    if root in (None,p,q): return root
    left = lcabinarytree(root.left,p,q)
    right = lcabinarytree(root.right,p,q)
    return root if left and right else  left or right