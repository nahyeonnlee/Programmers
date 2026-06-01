def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    total_set = set(range(1, n+1)) - lost_set
    
    
    for i in lost_set:
        if i-1 in reserve_set:
            total_set.add(i)
            reserve_set.remove(i-1)
        elif i+1 in reserve_set:
            total_set.add(i)
            reserve_set.remove(i+1)
            
        
    return len(total_set)