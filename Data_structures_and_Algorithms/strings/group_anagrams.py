# just use the letters in each word

def groupanagrams(strs):
    map={}
    for w in sorted(strs):
        key = tuple(sorted(w))
        map[key]=map.get(key,[])+[w]
    return map.values()