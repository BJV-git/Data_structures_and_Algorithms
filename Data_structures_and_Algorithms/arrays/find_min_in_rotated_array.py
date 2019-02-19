# for max we chase the end of continuous increasing order, now for min,

# trick the min is the next to the max, except oen case so do it

# the learned logic is that: know if its left rotated or right rotated

# works: based on the three numbers of the mid can make it work to see in which direction we can move

def rot_search(nums):
    if not nums: return -1

    lenn = len(nums)
    left = 0
    right = lenn - 1
    if nums[left] <= nums[right]:  # if not rotated
        return nums[left]

    while left <= right:

        if abs(left - right) == 1:
            return min(nums[left], nums[right])
        mid = (left + right) // 2
        # print(left, mid, right)
        if nums[mid] < nums[right] and nums[left] > nums[right]:
            right = mid
        elif nums[mid] > nums[left] and nums[mid] > nums[right]:
            left = mid
        elif nums[mid] < nums[right] and nums[left] > nums[mid]:
            right = mid


print(rot_search([4,5,6,7,8,9,2,3]))