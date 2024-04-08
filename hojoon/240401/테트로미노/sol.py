# 테트로미노
import sys
input = sys.stdin.readline

def dfs(x,y,step,total):
    global answer
    # 이건 4개일 때 조건이고, x,y 좌표 기준 모든 경우 탐색하면 어떻게 나가지?
    # 결국 일일이 탐색하고 그다음 dfs를 최종적으로 끝내는데 max_value를 통해 빨리 탈출
    if total + max_value*(4-step) <= answer:
        return
    if step == 4:
        answer = max(answer, total)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if step == 2:
                visited[nx][ny] = 1
                dfs(x,y,step+1,total+graph[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx,ny,step+1,total+graph[nx][ny])
            visited[nx][ny] = 0

n,m = map(int, input().split())
graph = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
max_value = 0 # 빠른 탐색 종료를 위한 변수
for i in range(n):
    graph.append(list(map(int, input().split())))
    max_value = max(max_value, max(graph[i]))
visited = [[0]*m for _ in range(n)]

answer = 0
for x in range(n):
    for y in range(m):
        visited[x][y] = 1
        dfs(x,y,1,graph[x][y])
        visited[x][y] = 0
print(answer)
