# so when we divide a word we set the [] index to be true so that from there we will check that if any
# other word fits from there

def word_break(s, map):
    ls = len(s)
    f=[False for i in range(ls+1)]
    f[0] = True
    for i in range(ls):
        if f[i]:
            for j in map:
                l = len(j)
                if l+i <= ls and s[i:i+l] == j:
                    f[i+l] = True
    print(f)
    return f[ls]


print(word_break('applesanbanana',['apples', 'and', 'banana'] ))