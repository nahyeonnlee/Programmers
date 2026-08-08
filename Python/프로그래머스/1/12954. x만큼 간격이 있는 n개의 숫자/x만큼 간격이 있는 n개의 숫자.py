def solution(x, n):
    answer = []
    init_x = x
    
    for i in range(n):
        answer.append(x)
        x += init_x
        
    return answer