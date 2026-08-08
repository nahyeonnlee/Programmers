import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) 
    
    # 첫번째 원소 스코빌 지수 < K
    while scoville[0] < K:
        
        # 예외처리
        if len(scoville) < 2:
            return -1
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        new_scoville = first + (second * 2)
        
        heapq.heappush(scoville, new_scoville)
        
        answer += 1
    
    return answer