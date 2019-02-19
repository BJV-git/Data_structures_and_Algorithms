# square
# sort
# start from last and have two indices to move to check if can find the triplets for each number

def pythagoren_triplets(nums):
    lnums=len(nums)
    triplets=0
    nums=[i**2 for i in nums]

    nums.sort()
    for i in range(lnums-1,-1,-1):
        j=0
        k=i-1

        while j<k:
            if nums[j]+nums[k] == nums[i]:
                triplets+=1
                break
            elif nums[j]+nums[k] < nums[i]:
                j+=1
            else:
                k-=1
    return triplets

print(pythagoren_triplets([1,3,4,5,6,7,8,10,11]))