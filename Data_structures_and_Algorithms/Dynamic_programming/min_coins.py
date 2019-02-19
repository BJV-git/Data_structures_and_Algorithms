import  sys

def mincoins(coins, target):
    table = [0 for i in range(target+1)]
    table[0]=0

    lc = len(coins)

    for i in range(1,target+1):
        table[i] = sys.maxsize

    for i in range(1,target+1):
        for j in range(lc):
            if coins[j]<=i:
                temp=table[i-coins[j]]

                if temp!=sys.maxsize and temp+1 < table[i]:
                    table[i] = temp+1

    return table[target]
