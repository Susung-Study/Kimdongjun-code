from collections import deque

dir = [(0,-1), (0,1), (-1,0), (1,0)]

def bfs(start, end, maps):
    n,m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    q = deque()
    flag = False
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == start:
                q.append((i,j,0))
                visited[i][j] = True
                flag = True
                break
        if flag == True: 
            break
            
    while q:
        x,y,c = q.popleft()
        
        if maps[x][y] == end:
            return c
        
        for d in dir:
            dx, dy = x+d[0], y+d[1]
            if 0<=dx<n and 0<=dy<m and maps[dx][dy] != 'X' and visited[dx][dy] == False:
                q.append((dx,dy,c+1))
                visited[dx][dy] = True
                
    return -1

def solution(maps):
    
    tolever = bfs('S', 'L', maps)
    toexit = bfs('L','E',maps)
    
    if tolever == -1 or toexit == -1:
        return -1
    
    return tolever+toexit
            