# learned logic: linked list is not as same as the list like accessing from middle
# we used inorder tracersal to convert from bst to sorted linked list
# so now need to use it reverse


# thought: first build teh nodes and then change the tree to bst
# thought works : of course we need to traverse that many times to find the middle

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def sortLLBst(head):
    if not head: return

    if not head.next : return TreeNode(head.val)

    slow , fast = head, head.next.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    temp = slow.next
    slow.next = None

    root = TreeNode(temp.val)
    root.left = sortLLBst(head)
    root.right = sortLLBst(temp.next)
    return root