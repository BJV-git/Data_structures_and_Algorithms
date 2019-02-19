# assuming when there are no duplicates in an array

# logic: use DFS; get one elem and then for every divided sub treat the same way to make sure all the combinations work out
# its a for loop and a dfs == back tracking


def permute(nums):
    res=[]
    dfs(nums,[],res)

    return res

def dfs(nums,path,res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

print(permute(['a','b','c','a']))