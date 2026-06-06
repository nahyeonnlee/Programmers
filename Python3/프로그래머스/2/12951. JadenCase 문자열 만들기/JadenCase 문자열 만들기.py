def solution(s):
    s_list = list(s.split(' '))
    for i in range(len(s_list)): 
        s_list[i] = s_list[i].capitalize()
        
    answer = ' '.join(s_list)
    
    return answer