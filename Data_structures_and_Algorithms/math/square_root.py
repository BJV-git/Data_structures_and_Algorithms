

def square_root(n):
    if n in (0,1):
        return n
    start=1
    end = n

    while (start<=end):
        mid = (start+end)//2
        prod = mid*mid

        if prod == n:
            return mid
        if prod < n:
            start = mid+1
            ans = mid
        else:
            end = mid-1
    return ans