def solution(s):
    sum_zero = 0
    sum_binary = 0
    
    while s != '1':
        sum_binary += 1
        count_zero = s.count('0')
        sum_zero += count_zero
        remain_len = len(s) - count_zero

        s = bin(remain_len)[2:]
        
    answer = [sum_binary, sum_zero]
    
    return answer 