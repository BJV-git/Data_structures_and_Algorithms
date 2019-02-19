#


def max_path(M):
    r,c = len(M), len(M[0])

    res=-1
    for i in range(c):
        res=max(res,M[0][i])

    for i in range(1,r):
        temp=-1
        for j in range(c):
            # all ways

            if j>0 and j < c-1:
                M[i][j] += max( M[i-1][j] , max(M[i-1][j-1], M[i-1][j+1]))
            elif j>0:
                M[i][j] += max(M[i-1][j-1], M[i-1][j])
            elif j < c-1:
                M[i][j] += max(M[i-1][j+1], M[i-1][j])

        res = max(M[i,j], res)

    return res