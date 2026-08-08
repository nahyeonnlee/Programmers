def solution(x):
    answer = True
    
    #자릿수 합
    sum_num = sum(int(i) for i in str(x))
    
    if x % sum_num != 0: answer = False
    
    return answer
