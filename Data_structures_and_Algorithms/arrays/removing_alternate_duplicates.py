# we cna maintain the dic to see if its even and then remove

# can do the same to the removing the duplicates of a str too


# logic: use dictionary to see if we encountered i.e. if 0 ro not there can remain if 1 then oonly eremove

# conatanty space as I am using dic of 26b length
def alettrnate_dups(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    map={i:0 for i in letters}
    res=''

    for i in s:
        if i.isalpha():
            if map[i]==0:
                res+=i
                map[i]+=1
            else:
                map[i]=0

        else:
            res+=i

    return res

print(alettrnate_dups('you got beautiful eyes'))