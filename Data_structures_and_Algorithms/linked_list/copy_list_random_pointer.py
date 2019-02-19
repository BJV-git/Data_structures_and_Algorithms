# use dictionary and then do but maintaining the memory is not effecient so better to create the node in run
# logic: put the new nodes in between while traversing firts

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

def copyRanndomList(head):
    if not head: return None

    p = head

    while p:
        node = RandomListNode(p.label)
        node.next = p.next
        p.next = node
        p=p.next.next # for inserting aftet the inserted new node

    p=head

    # time to move the random pointer

    while p:
        if p.random:
            p.next.random = p.random.next # here .next is used to point to the dummy or the one created
        p=p.next.next


    # time to remove the old connections

    newhead = head.next
    pold = head
    pnew = newhead

    while pnew.next:
        pold.next = pnew.next
        pold = pold.next
        pnew.next = pold.next
        pnew = pnew.next

    pold.next = None
    pnew.next = None

    return newhead