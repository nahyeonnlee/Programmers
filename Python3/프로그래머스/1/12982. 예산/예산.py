def solution(d, budget):
    answer = 0
    d.sort()
    
    for i in d:
        if budget >= i: #남은 예산 >= 이번 부서 지원금
            budget -= i
            answer += 1

    return answer