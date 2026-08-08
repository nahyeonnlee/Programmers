def solution(nums):
    N = len(nums)
    
    pks = set(nums)
    pks_types = len(pks)
    
    answer = min(pks_types, N/2)
    
            
    return answer