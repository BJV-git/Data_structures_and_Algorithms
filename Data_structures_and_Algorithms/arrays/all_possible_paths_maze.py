all_paths=[]

def findpath(maze):
    row, col = len(maze), len(maze[0])
    path=[0 for i in range(row+col-1)]
    findpaths(maze,row,col,0,0,path, 0)

def findpaths(maze,m,n,i,j,path,indx):
    global all_paths

    if i==m-1:
        for k  in range(j,n):
            path[indx+k-j] = maze[i][k]
        all_paths.append(path)
        return

    if j==n-1:
        for k in range(i,m):
            path[indx+k-i] = maze[k][j]
        all_paths.append(path)
        return

    path[indx] = maze[i][j]

    findpaths(maze,m,n,i+1,j,path,indx+1)
    findpaths(maze, m, n, i, j+1, path, indx + 1)

maze = [[1,2,3],
            [4,5,6],
            [7,8,9]]

findpath(maze)
print(all_paths)