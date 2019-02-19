# just will move a window of size n and will see the number of unique permutations and will see if count meets the req

# also we can skip to the next of outlier caz any ways wan
#

import collections

def anagram_substring(s, p):
        res=[]
        # first get the counters of both strings

        sc = collections.Counter(s[:len(p)-1])# it is -1 because on adding is the one we check and again we delete
        pc = collections.Counter(p)

        for i in range(len(p)-1, len(s)):
            sc[s[i]]+=1
            if sc==pc:
                res.append(i-len(p)+1)
            sc[s[i-len(p)+1]] -=1
            if sc[s[i-len(p)+1]] == 0:
                del sc[s[i-len(p)+1]]
        return res