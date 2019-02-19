# for constant space solution: do a dfs at every zero we encounter
# logic is encode decode : nwo here we are encoding in terms pf its row and column to mark if thats z zero ro w or column


def zeromatrix(matrix):
    row,col,first = len(matrix), len(matrix[0]), not all(matrix[0])

    for i in range(1,row):
        for j in range(col):
            if matrix[i][j]==0:
                matrix[0][j]= matrix[i][0] = 0

    for i in range(1,row):
        for j in range(col-1,-1,-1): # if there is first one zero, then entire row gets messed up as itis acting as ref
            if matrix[i][0] ==0 or matrix[0][j]==0:
                matrix[i][j]=0

    if first:
        matrix[0] = [0]*col