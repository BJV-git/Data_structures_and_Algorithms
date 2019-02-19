# logic : use the inorder to yield the value and then can constriuct the linked list just like that.

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def inorder(root):
    if root:
        inorder(root.left)
        yield root.val
        inorder(root.right)

    head = Node(-1)
    dummy = head

    in_val = inorder(root)

    bst = next(in_val)
    while bst:
        new = Node(bst)
        head.next = new
        head = head.next
    head.next =None

    return dummy.next