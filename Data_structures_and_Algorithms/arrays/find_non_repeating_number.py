# simple: use the xor function

def find_non_repeat(nums):

    if not nums: return False
    res=nums[0]
    for i in range(1,len(nums)):
        res^=nums[i]
    return res