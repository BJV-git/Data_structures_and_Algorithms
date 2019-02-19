# we can by maintainng a set and add only id not in set with O(n) time adn O(1) space

def remove_dups(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    map = {i: 0 for i in letters}
    res = ''

    for i in s:
        map[i] = map.get(i,0)+1
        if map[i] <2:
            res+=i
    return res

print(remove_dups('geekforgeeks'))