def solution(n):
    answer = 1 #자기 자신 카운트
    
    #1부터 n//2+1까지 탐색
    for i in range(1, n//2+1): 
        add = 0
        curr = i
        
        #현재 숫자에서 하나씩 더하가기
        while add < n:
            add += curr
            curr += 1
            
            #n과 같으면 answer 증가
            if add == n:
                answer += 1
                break
            
            #n 넘어버리면 break
            elif add >= n:
                break
                
    return answer