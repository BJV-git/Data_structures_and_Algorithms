# will make sure if the curr integer has the max to exceed the summ till that point else
# even though the curr_sum decreases the max_sum keeps track of the consecutive sum

# for indices can follow adding from both ends and output the max num indicex

def maxSubarray(nums):
    if not nums: return 0
    curr_sum=nums[0]
    max_sum=nums[0]

    for i in nums[1:]:
        curr_sum = max(curr_sum+i, i)
        max_sum = max(max_sum, curr_sum)

    return max(max_sum, curr_sum)