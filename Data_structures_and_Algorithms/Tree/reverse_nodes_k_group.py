# logic: write the reverse function with limit and repeat it along
# a good practice to create the a dummy node to carry the normal function with out extra case

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reversekgroup(head,k):
    dummy = jump = ListNode(-2)
    dummy.next = l = r = head

    while True:
        count=0
        while r and count < k:
            r = r.next
            count+=1

        if count ==k: # means we found out, with enough length,  that we can invert the list
            pre , cur =r,l
            for _ in range(k): # write the basic logic
                cur.next, cur, pre = pre, cur.next, cur
            jump.next, jump, l = pre, l, r # jump connecting ot new formed list; to the node we need to connect; the next list
        else:
            return dummy.next