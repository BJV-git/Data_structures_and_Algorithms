
def gcd(x,y):
    while y:
        x,y = y,x%y
    return x

def find_gcd(nums):


    a = nums[0]
    b=nums[1]

    g = gcd(a,b)

    lnums = len(nums)

    if lnums == 2:
        return g
    for i in range(2, lnums):
        g = gcd(g,nums[i])

    return g