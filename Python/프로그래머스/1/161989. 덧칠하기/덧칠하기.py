def solution(n, m, section):
    k = 0
    answer = 0
    
    for s in section:
        if k < s:
            k = s
            k += m-1
            answer += 1
        
    return answer