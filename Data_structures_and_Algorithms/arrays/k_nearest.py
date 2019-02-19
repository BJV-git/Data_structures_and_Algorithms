# always for the top k either big or small use the heap
# so simply form the dicionary with the points and their distances
import math
import heapq

def k_nearest(nums,p, k):
    map={}
    array=[]
    heapq._heapify_max(array)
    for i in nums:
        d = math.sqrt((nums[0]-p[0])**2 - (nums[1]-p[1])**2)
        if len(array) < k:
            array.append(d)
        elif heapq.nlargest(1,array)[0] > d:
            heapq._heappop_max()
            heapq.heappush(d)

        map[d] = tuple(i)

    for i in array:
        print(map[i])


array = [1,2,3,4,5,6]
heapq._heapify_max(array)


print(heapq._heappop_max(array))
print(heapq._heappop_max(array))
print(heapq._heappop_max(array))

print(array)

print(heapq.nlargest(1, array))
