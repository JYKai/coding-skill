from collections import deque

def bfs(graph, x, y, cnt):
    q = deque()
    q.append((x,y))
    graph[x][y] = cnt
    
    # dx, dy가 아니고 아예 연결관계로 봐야함 다익스트라처럼 현재 노드와 연결된애들
    # 각 행별로 행번호의 노드와 연결관계를 보이므로 행 단위로 탐색하면 됨
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    while q:
        qx, qy = q.popleft()
        
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 1:
                    q.append((nx,ny))
                    graph[nx][ny] = cnt

def solution(n, computers):
    answer = 0
    cnt = 2 # 같은 덩어리 종류로 구분하기 위함
    # 덩어리 문제라 생각하면 됨 >> 네트워크 = 덩어리
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            # 컴퓨터가 있다면 이어진 네트워크 있는지 탐색
            if computers[i][j] == 1:
                # 한번의 탐색에서 이어진 애들 연합으로 묶기(cnt)
                bfs(computers, i, j, cnt)
                # 다음 연합을 찾기 위해 cnt구분
                cnt += 1
                answer += 1       
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1
print(solution(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]])) # 2
print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]])) # 1
print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])) # 4
