# we are trying to trap the max bar on both sides and calculate the difference volume
# imagining the picture the water it can store is min(left_max, right_max) - its height as min is because water overflows
# so for calculating can maintain the maxes

def trap(bars):
    if len(bars) < 3:
        return 0

    vol=0

    l,r = 0, len(bars)-1
    l_max , r_max = bars[l], bars[r]

    while l<r:
        l_max = max(l_max, bars[l])
        r_max = max(r_max, bars[r])

        if l_max <= r_max:
            vol += l_max - bars[l]
            l+=1
        else:
            vol+=r_max - bars[r]
            r-=1
    return vol