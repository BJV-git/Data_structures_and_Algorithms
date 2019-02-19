# same as the number fo islands: its just that we place a dictionary and count the each ones total count

def largest_island(grid):
    row ,col = len(grid), len(grid[0])
    count=0
    map={}

    def nullify(r,c,p):
        possible = [[i,j] for i,j in ([r,c+1], [r,c-1],[r+1,c],[r-1,c]) if 0<=i<row and 0<=j<col]
        for i,j in possible:
            if grid[i][j]=='1':
                map[p] = map.get(p,0)+1
                grid[i][j]='0'
                nullify(i,j, p)

    for i in range(row):
        for j in range(col):
            if grid[i][j]=='1':
                print(i,j)
                grid[i][j]='0'
                count +=1
                p=(i,j)
                nullify(i,j,p)
    print(map)
    return count

print(largest_island([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))