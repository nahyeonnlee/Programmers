def solution(n,a,b):
    answer = 0
    
    # 같은 라운드에서 만날 때까지 반복
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
    
        answer += 1 
    
    return answer