def solution(nums):
    answer = 0
    
    N = len(nums)
    pick = N/2
    
    M = len(list(set(nums)))
    
    # 종류수가 전체 절반보다 적다면
    if M <= pick :
        return M
    else :
        return pick
