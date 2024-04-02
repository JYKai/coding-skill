def union(graph, x, cnt):
    for i in range(len(graph)):
        if graph[x][i] == 1:
            graph[x][i] = cnt
            graph[i][x] = cnt
            # 노드 x와 노드 i는 연결된 것이므로 i노드로 파고들기
            # 재귀로 부를 함수에 대해 return 하고 안하고 차이는 ?
            # 아마 함수 call stack이 다 비워지면 그 때 최종 return을 하기 때문에 이후의 탐색 안 한 i는 못 보는듯
            # call stack 한번 그려보기

            # call stack 그려봤을 때, 딱 한개의 길에 대해서만 탐색할거면 return
            # ex) (1->2) -> (2->2) return, 실제론 (1->4)로 가는 경로도 있지만 return 땜에 탐색 안 됨
            # 현재노드와 연결된 모든 연결관계 다 볼거면 return 안 해야
            return union(graph, i, cnt)
        
def solution(n, computers):
    answer = 0

    # 연결관계 파고 또 파고드는거라 dfs가 맞나?/ bfs론 어떻게 풀지
    # 연결관계 파고들어가며 같은 연합으로 묶기

    cnt = 2
    for row in range(n):
        for j in range(n):
            if computers[row][j] == 1:
                union(computers, row, cnt)
                cnt += 1
                answer += 1
    print(computers)
    return answer

#print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
#print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1
#print(solution(3, [[1, 0, 1], [0, 1, 0], [1, 0, 1]])) # 2
print(solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]])) # 1
#print(solution(4, [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])) # 4
