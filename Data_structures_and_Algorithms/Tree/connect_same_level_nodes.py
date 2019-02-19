# can use level order wed know and simply take the list to connect the rights consecutively

#learned logic: from top we will setup the next xonnextion so we can usethat to traverse to the next all childs


def connect_same_level_nodes(root):
    if not root: return None
    cur = root
    next = cur.left

    while cur.left:
        cur.left.next = cur.right

        if cur.next:
            cur.right.next = cur.next.left
            cur = cur.next
        else:
            cur = next
            next = cur.left