# just go on with the multiple and see if str(int has the kth digit

def nth_k_div(n,k):
    i=k-1
    while n:
        if i%k==0 or str(k) in str(i):
            n-=1
        if n==0:
            return i
        i+=1
    return i

print(nth_k_div(10,2))