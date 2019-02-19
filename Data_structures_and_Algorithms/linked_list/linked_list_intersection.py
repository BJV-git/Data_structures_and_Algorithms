# traverse two times recursively so that we know if == then , or else none

def intersect_ll(headA, headB):
    p,q = headA, headB

    while p!=q:
        p = p.next if p else headB
        q = q.next if q else headA
    return not p