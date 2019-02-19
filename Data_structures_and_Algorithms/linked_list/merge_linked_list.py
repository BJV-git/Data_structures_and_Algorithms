# whenevr we face a higher value we change or swap and move in that and if faced again we change again

def merge_linked_list(a,b):
    if a and b:
        if a.val > b.val:
            a,b = b,a
            a.next = merge_linked_list(a.next,b)
    return a or b