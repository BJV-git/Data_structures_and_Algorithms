# so we can start with [0,1] and then we can build on top of it each and every one
# for now just can build the strings so that if we have the 0 in last we append two to current and then ad
# if 1 then we gonna add only zero

# the comp no need to know this to c onstruct - better to find the sequence pattern and just find the number

# logic: makes sense as we add all the previous b i.e. 1 which add 0 at end, to a
# also a prev will have the same
# and b will get the 1s added to it


def  count(n):
    a = [0  for i in range(n)]
    b = [0  for i in range(n)]

    a[0] = b[0] = 1

    for i in range(1,n):
        a[i] = a[i-1] + b[i-1]
        b[i] = a[i-1]

    return a[n-1] + b[n-1]