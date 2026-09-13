def solution(numbers, target):
    answer = 0
    def dfs(index, current_sum):
        nonlocal answer #함수 바깥의 answer 사용
        
        #재귀 종료 조건
        if index == len(numbers):
            if target == current_sum:
                answer += 1
            return
        
        #다음 index에 + / - 케이스 재귀 호출
        dfs(index+1, current_sum + numbers[index])
        dfs(index+1, current_sum - numbers[index])
    
    #index=0, current_sum=0 부터 시작
    dfs(0, 0)
            
    return answer