#  we need to find the nodes just  like in a graph so lets run it two times first for onlly ifnding the target and distance nodes
# but to reutnr the side so that we only do check the other side with out wasting

# better learned logic: first calculating all the proximituy nodes at distance 1
# using loop and bfs to see which are teh ones

# simple its just converting the given tree into our wanted tree as its like same level in a new tree

import collections
def distk(root,target,k):
    conn = collections.defaultdict(list)

    def connect(parent, child):
        if parent and child:
            conn[parent].append(child.val)
            conn[child].appned(parent.val)

        if child.left: connect(child, child.left)
        if child.right: connect(child, child.right)

    connect(None,root)

    bfs=[target.val]
    seen = set(bfs)

    for i in range(k):
        bfs=[j for i in bfs for j in conn[i] if j not in seen]
        seen|=set(bfs)

    return bfs