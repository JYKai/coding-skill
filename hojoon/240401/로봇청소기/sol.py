# 로봇 청소기

# base : 현재칸 청소 안됐다면 청소하기

# 현재 기준 4면이 다 청소됐다면
# 바라보는 방향 유지하며 후진 > base조건 or 만약 후진이 안된다면 작동 멈춤 (탈출조건)

# 현재 기준 4면 중 청소 안된 곳이 있다면
# 반시계 90도 회전, 바라본 방향 기준으로 앞이 청소 안됐다면 전진 > base조건 수행

# 출력 : 작동 멈출 때 까지 청소하는 칸 개수
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,d,cnt):
    q = deque()
    q.append((x,y,cnt+1))
    visited[x][y] = 1
    graph[x][y] = 1
    while q:
        qx, qy, cnt = q.popleft()
        
        # 주변 탐색 > 3번 case
        if graph[qx+1][qy] == 0 or graph[qx-1][qy] == 0 or graph[qx][qy+1] == 0 or graph[qx][qy-1] == 0:
            # 3-1 실행, 현재 기준 반시계 회전
            for rotate in range(4): # for문 안하면 1번만 탐색함
                d -= 1
                if d == -1:
                    d = 3
                # 3-2 실행, 회전한 방향이 0인지 확인
                nx = qx + dx[d]
                ny = qy + dy[d]
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    # 전진
                    q.append((nx,ny,cnt+1))
                    # 방문하기 = 청소하기
                    visited[nx][ny] = 1
                    graph[nx][ny] = 1
                    break

        # 주변 탐색 > 2번 case (이미 청소했거나, 벽인 경우) > visited랑 구분이 안되네.. 걍 청소한곳 1로도 바꿔야 ? >> 바꿈
        elif graph[qx+1][qy] == 1 and graph[qx-1][qy] == 1 and graph[qx][qy+1] == 1 and graph[qx][qy-1] == 1:
            # 만약 뒤가 벽이라면 실행 멈춤 (종료 조건)
            nex = d-2 # 현재기준 머리 유지한채 뒤로만 이동하기 위한 변수 
            if nex < 0:
                nex += 4
            nx = qx + dx[nex]
            ny = qy + dy[nex]
            if visited[nx][ny] == 0:
                return cnt
            # 아니라면 후진 후 1번 반복
            q.append((nx,ny,cnt))

n, m = map(int, input().split())

# r,c 로봇이 처음 위치한 좌표
r,c,d = map(int,input().split())
# d : [0,1,2,3] = [북,동,남,서]
dy = [0,1,0,-1]
dx = [-1,0,1,0]

graph = []
for i in range(n):
    # 1: 벽, 0: 청소 해야하는 빈칸
    graph.append(list(map(int, input().split())))
# 방문여부 필요 > 2번 조건중 청소되지 않은 빈칸을 찾고 이동해야함
visited = [[0]*m for _ in range(n)]
answer = 0
answer = bfs(r,c,d,answer)

print(answer)
