# using tails i.e. storing the numbers such that if greater than all the previous ones can append else replace

def longest(nums):
    lnums=len(nums)
    tails=[0]*lnums

    size=0
    for n in nums:
        i,j = 0,size
        while i!=j:
            m=(i+j)//2
            if tails[m] < n:
                i=m+1
            else:
                j=m
        tails[i] = n

        size = max(1+i, size)
    return size