# the idea is to maintain the length of k, and then if some thing new comes just see the value to replace

import  heapq

class Kthlargest(object):
    def __init__(self, k, nums):
        self.nums = nums
        self.k =k

        heapq.heapify(self.nums)

        while len(self.nums) > self.k: # making sure we have the length
            heapq.heappop(self.nums)

    def add(self,n):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, n)
        else:
            heapq.heapreplace(self.nums, n)
        return self.nums[0]