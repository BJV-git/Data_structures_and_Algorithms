# can go and grab once ot get the total sum and then in second pass by removing can find

def middle_elem(nums):
    lnums = len(nums)

    right = left=0
    for i in range(1,lnums):
        right+=nums[i]

    j=1

    while j<lnums:
        right-=nums[j]
        left+=nums[j-1]

        if left==right:
            return nums[j]

        j+=1

