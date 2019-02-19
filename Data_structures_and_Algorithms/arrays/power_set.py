import math
def printpowerset(sett):
    pow_set_size = int(math.pow(2,len(sett)))

    counter=0
    j=0

    for counter in range(0,pow_set_size):
        for j in range(0,len(sett)):

            if counter & (1<<j)>0:
                print(sett[j], end='')

        print("")

def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])

    return x + [[l[0]] + y for y in x]


print(subs([1,2,3]))
print(printpowerset([1,2,3]))