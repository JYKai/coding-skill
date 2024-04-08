def back(curr, dungeons, visited, cnt):
    answer = cnt
    # 백트래킹
    for idx in range(len(dungeons)):
        # 아직 방문 안 했고, 현재 피로도가 요구 피로도보다 높다면
        if not visited[idx] and curr >= dungeons[idx][0]:
            visited[idx] = 1
            # max함수를 통해 이전 최대값(answer)와 현재값을 계속 비교하여 answer 갱신하기 때문에
            # answer가 현재값으로 덮어씌워지지 않고 최대의 값으로 반환가능함
            # max를 안해서 계속 answer값이 마지막에 했던 값으로 덮어 씌워진 것
            answer = max(answer, back(curr - dungeons[idx][1], dungeons, visited, cnt+1))
            visited[idx] = 0
    return answer
    
def solution(k, dungeons):
    answer = -1
    visited = [0] * len(dungeons)

    # 여기의 루프는 첫시작을 정하는 loop, 이후 경우의 수 뻗기는 back에서 재귀로 시행
    # for idx in range(len(dungeons)):
    #     visited = [0] * len(dungeons)
    #     answer = max(answer, back(k, dungeons, visited, 0))

    # 그럴 필요 없이 back에서 처음부터 시행 가능
    answer = back(k, dungeons, visited, 0)
    return answer
