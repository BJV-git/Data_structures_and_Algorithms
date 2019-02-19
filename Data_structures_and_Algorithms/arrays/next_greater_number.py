# will see if we can swap as same logic used in next permutation
#just like how human do

def next_great_number(n):
    digits = list(str(n))
    l = len(digits)

    i,j = l-2,l-1

    while i>=0 and digits[i] >= digits[i+1]:
        i-=1

    if i==-1: return -1

    while digits[j] <= digits[i]:
        j-=1

    print(j)
    exit()

    digits[i], digits[j] = digits[j], digits[i]

    res=int(''.join(digits[:i+1]+digits[i+1:][::-1]))

    if res>= 2**31 or res==n:
        return -1
    return res

print(next_great_number(123465))