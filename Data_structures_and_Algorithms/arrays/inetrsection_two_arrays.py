# intersection of two arrays; just the numbers

# can do using sets but better if can use the dict
# even simpler is to maintain a set for top and see if exists

def common_elem(a,b):
    map={}
    res=[]

    for i in a:
        map[i] = map.get(i,0)+1
    for i in b:
        if i in map and map[i]>0:
            res.append(i)
            map[i]=0 # map[i]-=1 # for gettig all teh elements
    return res