def longest_palin(s):
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P=[0]*n
    C=R=0

    for i in range(1,n-1):
        P[i] = (R>i) and min(R-i,P[2*C-i])

        while T[i+1+P[i]]==T[i-1-P[i]]:
            P[i]+=1

        if i+P[i] > R:
            C,R = i, i+P[i]


    maxi, center = max((n,i) for i,n in enumerate(P))
    return s[(center-maxi)//2:(center+maxi)//2]

a=2
b=3

p=(b<a) and max(5,6)
print(p)