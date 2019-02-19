def counts(coins, target):
    lc = len(coins)
    table = [[0 for x in range(lc)] for y in range(target+1)]

    for i in range(lc):
        target[0][i]=1

    for i in range(1, target+1):
        for j in range(lc):
            x = table[i-coins[j]] if i-coins[j]>=0 else 0

            y = table[i][j-1] if j>= 1 else 0

            table[i][j] = x+y

    return table[target][lc-1]


