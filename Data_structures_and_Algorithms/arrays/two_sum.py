# maintain a dict and then check

# if we look at  number we are storing the target number, if found return
# simply can add to seen

def two_sum(nums,k):
    buff_dict={}
    lnums = len(nums)
    if lnums<=1:
        return False

    for i in range(lnums):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[k - nums[i]] = i

    lnums = len(nums)
    if lnums <= 1:
        return False
    seen = set()
    for i in range(lnums):
        print(i, seen)
        if nums[i] in seen:
            return [nums[i], target - nums[i]]
        else:
            seen.add(target - nums[i])