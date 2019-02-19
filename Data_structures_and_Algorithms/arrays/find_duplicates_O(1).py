# if array has n elem and all are 0 to n-1 then finding the nums is done in O(n) and O(1)
# this is done by takinng the advantage of the indices as they are sorted and can see if the number in that index is negative or not
# more over the nubers are indices and the indices are the numbers

def find_duplicates(nums):
    lnums = len(nums)
    for i in range(lnums):
        if nums[abs(nums[i])]>=0:
            nums[abs(nums[i])] = -nums[abs(nums[i])]
        else:
            print(abs(nums[i]))
    print(nums)

print(find_duplicates([1,2,3,1,3,5]))