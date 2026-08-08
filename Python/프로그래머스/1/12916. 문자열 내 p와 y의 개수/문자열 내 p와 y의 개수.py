def solution(s):
    answer = True
    p_t = 0
    y_t = 0
    
    s = s.lower()
    
    for i in s:
        if i == 'p': 
            p_t += 1
        elif i == 'y':
            y_t += 1
    
    if p_t != y_t:
        answer = False
        
    return answer