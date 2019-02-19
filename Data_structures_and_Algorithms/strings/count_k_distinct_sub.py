# normal count strategy

def countk(s,k):
    n = len(s)
    res=0
    for i in range(0,n):
        dist_count=0
        map={i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}

        for j in range(i,n):

            if map[s[j]]==0:
                dist_count+=1

            map[s[j]]+=1

            if dist_count==k:
                res+=1
            if dist_count>k:
                break

    return res

print(countk('pqpqs',2))