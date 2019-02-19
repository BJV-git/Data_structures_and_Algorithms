# count for both the freq and diff take

def make_anagram_del(a,b):
    mapa ={}

    for i in a:
        mapa[i] = mapa.get(i,0)+1
    for j in b:
        mapa[j]-=1

    return sum(mapa.values())