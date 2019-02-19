# same as all permutations however when the permutations aree allowed
# the index avoids adding the same element in different places as it woudld be just 0 all the time or just the initial position

def permuUnique(nums):
    perms=[[]]
    for i,n in enumerate(nums):
        perms = [ p[:i]+[n]+p[i:] for p in perms for i in range((p+[n]).index(n)+1)] # here i is the position we add the new number

    print(perms)

permuUnique(['a','b','c','a'])

