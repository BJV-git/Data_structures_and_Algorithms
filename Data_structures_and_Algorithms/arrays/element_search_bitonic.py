#

def find(nums, low, high):
    if low == high:
        return nums[low]

    if high==low+1:
        return min(nums[low], nums[high])

    mid = (low+high)//2

    if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
        return nums[mid], mid

    if nums[mid+1] < nums[mid] < nums[mid-1]:
        return find(nums,low, mid-1)
    else:
        return find(nums, mid+1, high)


def find_x(nums,x):
    maxi , ind= find(nums, 0,len(nums)-1)

    if x> maxi:
        return None
    elif x==maxi:
        return ind

    low =0
    high = ind-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==x:
            return mid
        if nums[mid] > x:
            high = mid-1

        else:
            low = mid+1

    low=ind+1
    high = len(nums)-1

    while low<=high:
        mid=(low+high)//2
        if nums[mid]==x:
            return mid

        if nums[mid] < x:
            high = mid-1
        else:
            low=mid+1

    return -1