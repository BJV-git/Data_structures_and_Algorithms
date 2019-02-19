def isvalid(maze,x,y):
    if x>=0 and x< len(maze) and y>=0 and y < len(maze) and maze[x][y]==1:
        return True
    return False

def solvemaze(maze):
    n = len(maze)
    sol=[[0 for i in range(n)] for i in range(n)]
    if solvemazeutil(maze,0,0,sol)==False:
        print('no man')
    else:
        print(sol)
global n
def solvemazeutil(maze,i,j,sol):
    if i==n-1 and j==n-1:
        sol[i][j]=1
        return True
    if isvalid(maze,i,j)==True:
        sol[i][j]=1

        if solvemazeutil(maze, i+1, j, sol)==True:
            return True
        if solvemazeutil(maze, i, j+1, sol) == True:
            return True

        sol[i][j]=0
        return False