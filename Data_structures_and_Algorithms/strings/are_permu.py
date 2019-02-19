# simply can count

def are_permu(a,b):
    map={}
    for i in a:
        map[i] = map.get(i,0)+1
    for j in b:
        try:
            map[j]-=1
            if map[j]<0:
                return False
        except:
            return False
