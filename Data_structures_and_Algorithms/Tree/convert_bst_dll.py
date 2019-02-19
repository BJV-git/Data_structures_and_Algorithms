# logic: can define the inorder and then yeidl while just converting the dll

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

def inorder(root):
    if root:
        inorder(root.left)
        yield root.val
        inorder(root.right)

    head = Node(-1)
    tail = Node(-2)
    head.next = tail
    tail.prev = head

    dummy = head

    in_val = inorder(root)

    bst = next(in_val)
    while bst:
        bst = next(bst)
        new = Node(bst)
        head.next = new
        new.prev = head
        new.next = tail
        tail.prev = new
        head = head.next


    return dummy.next