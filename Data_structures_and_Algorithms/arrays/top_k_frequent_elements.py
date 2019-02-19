# logic: plain
# to keep track of the counts and then just output the most frequent

def topKFrequent(self, nums, k):
    dic = {}
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    dic = sorted(dic, key=lambda x: dic[x], reverse=True)
    return dic[:k]