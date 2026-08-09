def solution(n):
    
    #n의 1개수
    one = bin(n).count('1')
    
    next = n+1
    
    while True:
        #n보다 큰 숫자 1 개수
        next_one = bin(next).count('1')
        
        #1 개수 같을 때 반환
        if one == next_one:
            return next
        
        next += 1
        