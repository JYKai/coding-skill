wheel = []
for i in range(4):
    wheel.append(list(map(int,input().rstrip())))

def dfs(current, wise, cnt):
    # 양 끝 바퀴를 벗어나면 반환
    if current > 3 or current < 0:
        return
    # 3시 방향, 9시 방향 극 알아두기
    right = wheel[current][2]
    left = wheel[current][6]
    
    # 시계 방향이라면
    if wise == 1:
        # 해당 톱니 회전 시키기
        wheel[current] = [wheel[current][-1]] + wheel[current][:-1]
        if 1 <= current < 3:
            # 옆 바퀴 와 체크하기, 다르다면 반대로 회전
            if wheel[current-1][2] != left:
                dfs(current-1,-wise, cnt+1)
            if wheel[current+1][6] != right:
                dfs(current+1,-wise, cnt+1)
        elif current == 0 and cnt == 0:
            if wheel[current+1][6] != right:
                dfs(current+1,-wise, cnt+1)
        elif current == 3 and cnt == 0:
            if wheel[current-1][2] != left:
                dfs(current-1,-wise, cnt+1)
                
    # 반시계라면
    else:
        wheel[current] = wheel[current][1:] + [wheel[current][0]]
        if 1 <= current < 3:
            if wheel[current-1][2] != left:
                dfs(current-1,-wise, cnt+1)
            if wheel[current+1][6] != right:
                dfs(current+1,-wise, cnt+1)
        elif current == 0 and cnt == 0:
            if wheel[current+1][6] != right:
                dfs(current+1,-wise, cnt+1)
        elif current == 3 and cnt == 0:
            if wheel[current-1][2] != left:
                dfs(current-1,-wise, cnt+1)
                
k = int(input())
answer = 0
for _ in range(k):
    print(f"before {wheel}")
    norm, wise = map(int, input().split())
    dfs(norm-1, wise, 0) # index접근이라 실제 톱니번호보단 1 작게 넣기
    print(f"after {wheel}")

for i in range(4):
    # S극 이라면
    if wheel[i][0] == 1:
        # answer += ((i)*(2))*wheel[i][0]
        answer += 2**i
print(answer)

    
