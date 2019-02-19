# use recurisve formuala till we get a 1 in power but as if we find odd we need one more extra

def power(a,b):
    if b==0:
        return 1
    elif b%2==0:
        return power(a,b//2)*power(a,b//2)
    else:
        return a*power(a,b//2)*power(a,b//2)

print(power(2,2))