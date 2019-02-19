# logic: have a dictionary to count all teh pairs and then divide as we counted twice


def all_pairs(nums, k):
    map={}
    res=0
    for i in nums:
        map[i]=map.get(i,0)+1

    for i in nums:
        diff=k-i
        if diff in map:
            res+=map[diff]
        if i*2 == k:
            res-=1
    return res//2

print(all_pairs([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1],11))