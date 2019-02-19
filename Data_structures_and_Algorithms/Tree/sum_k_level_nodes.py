# can use the level order traversal and then giev

def sum_k_level(root,k):
    if not root: return 0
    res,queue=[],[root]
    count=0

    while queue:
        queue = [child for node in queue for child in (node.left, node.right) if child]
        count+=1
        if count==k:
            res=[i.val for i in queue]
            return sum(res)