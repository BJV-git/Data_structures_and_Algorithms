# have two pointers and move in accordance to comparision and then pop when met the kth
# the whole idea is to eliminate k/2 elements rather /2 of the given arrays of larger lengthgs

# can be used for median too, as its just the middle element

def kth_two_sorted_arays(a,b,k):

    if len(a) > len(b):
        return kth_two_sorted_arays(b,a,k)

    if not a:
        return b[k]

    if k== len(a)+len(b)-1:
        return min(a[-1], b[-1])

    i=len(a)//2
    j = k-1

    if a[i] < b[j-1]:
        return kth_two_sorted_arays(a[i:], b[:j], j)
    else:
        return kth_two_sorted_arays(a[:i],b[j:], i)


