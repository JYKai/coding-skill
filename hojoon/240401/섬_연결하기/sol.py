def find(parent, x):
    # x의 부모가 x와 다르면 x 부모찾기
    if parent[x] != x:
        return find(parent, parent[x])
    return parent[x]
def union(parent,a,b):
    a = find(parent, a)
    b = find(parent, b)
    # a,b 정보가 뭐지 ? (노드 번호)이며 노드 번호가 작을 수록 레벨이 낮음 (root쪽)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

def solution(n, costs):
    answer = 0
    # 각 노드들의 부모 노드들 저장
    parent = [0]*n
    # 우선 부모는 자기 자신으로 설정
    for i in range(n):
        parent[i] = i
    
    edges = []
    for i in costs:
        a, b, cost = i
        edges.append((cost,a,b))
    # 노드정보 cost 기준으로 오름차순 정렬
    edges.sort()
    
    for edge in edges:
        cost, a, b = edge
        # a, b의 부모가 다르다면 > 연결관계 x > 이어주기
        # 만약 둘의 부모가 같다면 이미 이어진 상황이므로 연결할 필요 x
        # 그리고 이미 cost순으로 정렬하고 최소값들 먼저 이은 것이므로 이후는 연결할 필요 x
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
            
    return answer
