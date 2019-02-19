# simple logic: count and see in its one or use set

def uniq_two_arrays(a,b):
    map={}
    res=[]
    for i in a:
        map[i] = map.get(i,0)+1
    for j in b:
        map[j] = map.get(j,0)+1

    for i in map:
        if map[i]==1:
            res.append(i)
    return res