# logic: just keep the left most or first most values in teh level order traversal
# or right side view replace with -1

def leftsideview(root):
    view=[]
    if root:
        level=[root]
        while level:
            view +=level[0].val, # if not placed comma it wouldnt work
            level = [kid for node in level for kid in (node.left , node.right) if kid]
    return view