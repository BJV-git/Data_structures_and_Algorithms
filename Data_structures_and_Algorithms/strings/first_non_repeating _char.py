# isntead of maintaingin a dict lets mainatain a row of all alphabets

def firtsUnique(s):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    count={}
    for i in s:
        count[i] = count.get(i,0)+1
    indices=[s.index(l) for l in alp if count[l]==1]

    return min(indices) if indices else -1