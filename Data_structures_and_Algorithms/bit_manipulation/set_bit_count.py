# can use >> to shift and & with 1

def set_count(n):
    count=0
    while n:
        count+=n&1
        n>>=1
    return count

print(set_count(2))