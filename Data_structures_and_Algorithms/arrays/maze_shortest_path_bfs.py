def isvalid(maze,x,y):
    if x>=0 and x< len(maze) and y>=0 and y < len(maze) and maze[x][y]==1:
        return True
    return False

def bfs(maze, start, end):
    rows=[-1,0,0,1]
    cols=[0,-1,1,0]

    if not maze[start[0]][start[1]] or not maze[end[0]][end[1]]:
        return -1

    r,c = len(maze), len(maze[0])

    visited=[[False for i in range(c)] for i in range(r)]

    visited[start[0]][start[1]] = True

    queue=[start,0]

    while queue:
        point , dist= queue.pop(0)
        if point == end:
            return dist

        for i in range(r):
            if isvalid(maze,point[0]+rows[i], point[1]+cols[i]):
                queue.append([point[0]+rows[i], point[1]+cols[i]])



    return -1