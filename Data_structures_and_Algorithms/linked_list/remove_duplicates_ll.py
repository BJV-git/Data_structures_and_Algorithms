# learned: simply skip the duplicate node

def remove_duplicate(head):
    cur=head
    while cur: # for move on
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        cur = cur.next
    return head