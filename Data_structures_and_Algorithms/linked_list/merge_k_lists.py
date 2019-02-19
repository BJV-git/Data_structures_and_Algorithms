# logic: have a priority queue then can call the next element eahc time and the queue adjusts accoerding to the value

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
from queue import PriorityQueue
def merge_k_lists(lists):
    dummy =ListNode(None)
    curr=dummy

    p=PriorityQueue()

    for node in lists:
        if node: p.put((node.val, node))
    while p.qsize()>0:
        curr.next = p.get()[1]
        curr=curr.next
        if curr.next: p.put((curr.next.val, curr.next))

    return dummy.next