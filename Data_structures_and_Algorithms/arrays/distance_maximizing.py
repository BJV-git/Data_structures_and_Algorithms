# so we have to find the indices j-i is max so that arr[j > other,
# come from right, take the max and see if we can find the min, change the max so that - its is > min indie adn prev max
# change the min if the diff is > prev diff

# we can first amrk which can be eligible starting points i.e. for whihc are increasing as they is no point is checking others
# video: https://www.youtube.com/watch?v=zUwQBUtRgJg

# so first we need to mark the possible starts and start from the other end, adn approach linearly

def maxDist(arr):
    larr= len(arr)
    lmin=[0]*larr
    rmax=[0]*larr
    max_diff=-1

    lmin[0] = arr[0]

    mins=[[0,arr[0]]]

    for i in range(1,larr):
        if arr[i] < mins[-1][1]:
            mins.append([i,arr[i]])

    j = larr-1
    i = len(mins)-1

    while j>0 and i>0:
        if mins[i] > arr[j]:
            max_diff = max(max_diff, j-i)
            j-=1
        else:
            i-=1

    return max_diff



    # for i in range(1,larr):
    #     lmin[i] = min(arr[i], lmin[i-1])
    #
    # rmax[larr-1] = arr[larr-1]
    #
    # for j in range(larr-2,-1,-1):
    #     rmax[i] = max(arr[i], rmax[i+1])
    #
    # i,j=0,0
    # maxdiff=-1
    #
    # while i <