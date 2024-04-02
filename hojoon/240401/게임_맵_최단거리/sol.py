from collections import deque

def bfs(graph, x, y):
    visited = [[0]*len(graph[0]) for _ in range(len(graph))]
    q = deque()
    q.append((x,y,1))
    visited[x][y] = 1
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    while q:
        qx, qy, cnt = q.popleft()
        
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    q.append((nx,ny,cnt+1))
                    visited[nx][ny] = 1
                # 상대방 진영에 도달했다면
                if nx == len(graph)-1 and ny == len(graph[0])-1:
                    return cnt+1
    return -1 # while문 나왔다면 -1 반환

def solution(maps):
    answer = bfs(maps, 0, 0)
    
    return answer
