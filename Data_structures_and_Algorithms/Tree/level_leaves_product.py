# will use the bfs to see all the nodes and add if we have leaves by checking

import  numpy as  np

def level_leaves_prod(root):
    if not root: return 0
    bfs=[root]
    res=[]

    while bfs:
        res.append( sum([i.val for i in bfs if not i.left and not i.right]))
        bfs = [child for node in bfs for child in (node.left, node.right) if child]

    return np.prod(res)