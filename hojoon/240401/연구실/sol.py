from collections import deque

def back(walls):
    global answer
    
    if walls == 3:
        virus = deque()
        # deepcopy 대신 이렇게 복사하기
        copied = [[graph[x][y] for y in range(m)] for x in range(n)]
        for x in range(n):
            for y in range(m):
                if graph[x][y] == 2:
                    virus.append((x,y))
        
        while virus:
            vx, vy = virus.popleft()
            
            for i in range(4):
                nx = vx + dx[i]
                ny = vy + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if copied[nx][ny] == 0:
                        copied[nx][ny] = 2
                        virus.append((nx,ny))
        cnt = 0
        for x in range(n):
            for y in range(m):
                if copied[x][y] == 0:
                    cnt += 1
        answer = max(answer, cnt)
        return 
    
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                graph[x][y] = 1
                back(walls+1)
                graph[x][y] = 0
                
n, m = map(int, input().split())
answer = 0
graph = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    graph.append(list(map(int, input().split())))

for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            graph[x][y] = 1
            back(1)
            graph[x][y] = 0
print(answer)
