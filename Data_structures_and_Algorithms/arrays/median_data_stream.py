# so lets add number by number
# so when we add we store total number and two things we can see if total is odd then if number is on right or lefy or middle
# we shift the gear,

# if its even based on current number we shift to left or right or so

# ??? for shifting we need the things to be ordered
# else for that I can store a set and then can make a move by decrementing mormally by 1

from heapq import *

class Meanfinder(object):

    def __init__(self):
        self.small=[]
        self.large=[]

    def add(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num)) # -num as we want the largest in top
        else:
            heappush(self.small, -heappushpop(self.large, num)) # caz we want to do it as max heap so -heapush

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0])/2.0
        else:
            return float(self.large[0])


small=[-2]

x = -heappushpop(small, -4)
print(small, x)