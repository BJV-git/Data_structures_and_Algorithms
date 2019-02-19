# logic: is to convert the numbers into different base so that we can sort in O(kn) times where k is numbe of digits in the
# n2-1 item

def countsort(nums, exp):
    lnums=len(nums)
    output=[0]*lnums
    count=[0]*lnums

    for i in range(lnums):
        count[(nums[i]//exp)%lnums] +=1
    print(count)
    for i in range(lnums):
        count[i] += count[i-1]

    print(count)

    for i in range(lnums-1,-1,-1):
        output[count[(nums[i]//exp)%lnums]-1] = nums[i]
        count[(nums[i]//exp)%lnums] -=1
    print(output)

print(countsort([0,10,13,12,7], 1))