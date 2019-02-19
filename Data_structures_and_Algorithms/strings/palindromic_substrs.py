def countsubpalin(S):
    def manachers(S):
        A='^#'+'#'.join(S) + '#$'
        Z=[0]*len(A)
        center=right=0

        for i in range(1,len(A)-1):
            if i < right:
                Z[i] = min(right-i,Z[2*center-i])
            while A[i+Z[i]+1] == A[i-Z[i]-1]: # trying to see if can expand beyond the existing stuff
                Z[i]+=1
            if i+Z[i] > right: # if happen to extend successfully then we can update center and right
                center, right = i,i+Z[i]

        return Z

    return sum((v+1)//2 for v in manachers(S))