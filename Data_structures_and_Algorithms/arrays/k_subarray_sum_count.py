# logic similar to fb friends
# have the window and move so that have the sum for each elem just add and subtract

def sub_array_k_count(nums,k,summ):
    lnum = len(nums)
    if k>lnum:
        return 0

    temp=sum(nums[:k])
    count=0

    i=0
    j=k

    while j < lnum:
        temp+=nums[j]
        temp-=nums[i]

        if temp==summ:
            count+=1
        i+=1
        j+=1
    return count