import  random

def random_sort(nums):
    for i in range(len(nums)-1,-1,-1):
        rand_int = random.randint(0,i+1)
        nums[i], nums[rand_int] = nums[rand_int], nums[i]

    return nums