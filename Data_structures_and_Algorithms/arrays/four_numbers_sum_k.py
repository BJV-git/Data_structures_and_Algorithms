# logic: O(n3)

def four_sum_k(nums,k):
    nums.sort()
    lnums=len(nums)

    for i in range(lnums-3):
        for j in range(i+1, lnums-2):
            l=j+1
            r = lnums-1


            while (l<r):
                summ = nums[i]+nums[j] + nums[l] + nums[r]
                if summ==k:
                    l+=1
                    r-=1

                elif summ < k:
                    l+=1

                else:
                    r-=1