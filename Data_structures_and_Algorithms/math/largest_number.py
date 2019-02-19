#actually can solve if we can extend teh single digit padded with same to match length and can compare

# i think it can be done with concatning as we concatnate we can combine, based on the length, 

# logic: rewriting the cmp logic

def largest_num_formed(nums):
    nums=[str(x) for x in nums]
    nums.sort(cmp=lambda a,b: (b+a, a+b))
    return ''.join(nums).lstrip('0') or 0