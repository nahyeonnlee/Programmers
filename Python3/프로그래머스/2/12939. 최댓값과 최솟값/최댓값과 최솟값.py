def solution(s):
    numbers = list(map(int, s.split()))
    max_num, min_num = max(numbers), min(numbers)
    
    answer = str(min_num) + ' ' + str(max_num)
    return answer