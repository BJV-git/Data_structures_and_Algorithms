# for the closest I need to verify the successor and predesecor and see teh difference to return the number
# keeping track of the closest and if we dont find return the closest found so far

# simple

def findnearest(head, k, min_diff, minimum):
    if not head: return

    if head.val == k:
        minimum = k
        return
    if min_diff > abs(k-head.val):
        min_diff = abs(k-head.val)
        minimum = head.val

    if k < head.val:
        findnearest(head.left, k, min_diff, minimum)
    else:
        findnearest(head.right, k, min_diff, minimum)

findnearest(head,k,sys.maxsize,-1)