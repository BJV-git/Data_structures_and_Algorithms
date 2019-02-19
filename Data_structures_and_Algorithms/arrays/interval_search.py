# first merge the intervals and then search for the one in liinear time

def merge(nums):
    nums.sort(key=lambda x: x[0], revers = True)

    stack=[]
    for n in nums:
        p = nums.pop(0)
        if not stack:
            stack.append(p)
        if stack[-1][1] < p[0]:
            stack.append(p)
        elif stack[-1][1] < p[1]:
            stack[-1][1] = p[1]

    # so sorted and all r in increasing way with the overlaps taken care
    key=None
    ind=0

    for i in stack:
        if key < i[1]:
            return ind+i[1] - key
        else:
            ind += (i[1]-i[0])
    return False