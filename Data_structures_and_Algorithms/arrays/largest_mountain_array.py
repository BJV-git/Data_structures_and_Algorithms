# have two pointers so that can move, end : if both == false elif >=3 return len
# when faced the end we have to reset the start one

# count the ups and downs and updated when faced a downhil while decreasing
def largest_mountain(nums):
    maxi = up=down=0
    for i in range(1,len(nums)):
        if down and nums[i-1] <= nums[i]: up=down=0
        up+= nums[i-1] < nums[i]
        down+= nums[i-1] > nums[i]
        if up and down :maxi = max(maxi, up+down+1)
    return maxi

m=[1,2,3,4,5,4,3,2,1]
up=0
up+=m[3] < m[4]

print(up)