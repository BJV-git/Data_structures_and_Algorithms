# just about the positional ordering

# just can go by the next.next and set the odd last to even head

def odd_even(head):
    if not head or not head.next: return head

    odd =head
    even = head.next
    evenhead = head.next

    while even and even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = evenhead
    return head