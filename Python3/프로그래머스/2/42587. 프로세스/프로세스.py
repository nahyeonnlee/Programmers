from collections import deque

def solution(priorities, location):
    answer = 0
    
    #(location, priority)형태로 큐에 저장
    queue = deque(enumerate(priorities))
    
    while queue:
        p = queue.popleft()
        
        # 큐에 다른 프로세스 남아 있고, 나온 프로세스보다 우선 순위 높은 게 있다면
        if queue and p[1] < max(x[1] for x in queue):
            queue.append(p)
        # 나온 프로세스보다 우선 순위 높은 게 없다면
        else:
            answer += 1
            
            # 내가 찾는 location과 같은지 확인
            if p[0] == location:
                return answer
