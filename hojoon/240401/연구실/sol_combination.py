# 0 : 빈칸, 1: 벽, 2: 바이러스
# 벽 3개를 추가적으로 세우고, 바이러스 확산시 안전한 칸 개수 반환
# 안전한 칸 중 최대값 구하기 >> 순열 or 백트래킹

import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
input = sys.stdin.readline

def bfs(copied, virus):
    cnt = 0

    while virus:
        qx, qy = virus.popleft()
        # 바이러스 확산
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            # 범위조건 만족하고 다음칸이 빈칸이면 확산
            if 0 <= nx < n and 0 <= ny < m and copied[nx][ny] == 0:
                # 연구소 바이러스 확산
                copied[nx][ny] = 2
                # 바이러스 좌표 저장
                virus.append((nx,ny))
    # 안전지대 카운트
    for i in range(n):
        for j in range(m):
            if copied[i][j] == 0:
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = []
candidates = []
virus = deque()
dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(len(graph[0])):
        # 벽 3개 세울 후보 찾기
        if graph[i][j] == 0:
            candidates.append((i,j))
        # 바이러스 시작지 바로 접근하기 위해 저장
        elif graph[i][j] == 2:
            virus.append((i,j))

# 3개 조합 찾기
candidates = list(combinations(candidates, 3))
answer = 0
# 각 3개의 벽후보마다의 확산개수 구하기
for candidate in candidates:
    # 그래프 초기화
    copied = deepcopy(graph)
    vir = deepcopy(virus)
    a,b,c = candidate
    copied[a[0]][a[1]] = 1
    copied[b[0]][b[1]] = 1
    copied[c[0]][c[1]] = 1
    answer = max(answer,bfs(copied,vir))
print(answer)
