# normal window and count strategy

def longest_k(s,k):
    ls = len(s)
    map = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}
    uniq=0

    for i in s:
        if map[i]==0:
            uniq+=1
        map[i]+=1

    if uniq < k:
        print('wrong input')
        return None

    curr_start=0
    curr_end = 0

    max_win = 1
    max_start = 0

    map = {i: 0 for i in 'abcdefghijklmnopqrstuvwxyz'}

    map[s[0]] +=1

    for i,j in enumerate(s,1):
        map[j] +=1
        curr_end+=1

        while k >= sum((i for i in map if map[i]>0)):
            map[s[curr_start]]-=1
            curr_start+=1
        if curr_end-curr_start+1 > max_win:
            max_win = curr_end-curr_start+1
            max_start = curr_start

