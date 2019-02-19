# can maintain a dictionary of letters and their positionings so that if all are seperated by not more than 1 then permutation
# exists

# maintaining a target to see the count of the variables we need ot find
# window will count to the length of the a, and will subtract the things we might not need
# when == true else false

def str_permu(a,b):
    A = [ord(x)-ord('a') for x in a]
    B = [ord(x) - ord('a') for x in b]

    target = [0]*26
    for i in A:
        target[i]+=1

    window=[0]*26

    for i,x in enumerate(B):
        window[x]+=1
        if i >= len(A):
            window[B[i-len(A)]]-=1
        if window==target:
            print(i)
            print(target, 'target')
            print(window, 'window')
            return
    return False


str_permu('ab', 'eiabo')