# we can do the computation in O(logn)
# O(N) is just by having those two previous values and then just add up

'''If n is even then k = n/2:
F(n) = [2*F(k-1) + F(k)]*F(k)

If n is odd then k = (n + 1)/2
F(n) = F(k)*F(k) + F(k-1)*F(k-1)'''



def nth_fibonnacii(n):
    f=[0]*1000

    def fib(n):
        if n==0:
            return 0
        if n in (1,2):
            f[n] = 1
            return f[n]
        if f[n]:
            return f[n]

        if(n & 1 ):
            k = (n+1)//2
        else:
            k = n//2

        if (n&1):
            f[n] = (fib(k) *fib(k) + fib(k-1)*fib(k-1))
        else:
            f[n] = (2*fib(k-1) + fib(k))*fib(k)

        return f[n]

    fib(n)
    return f[n]

print(nth_fibonnacii(9))